import requests
from bs4 import BeautifulSoup
import constants
from collections import namedtuple
import datetime
import json

SVFU_URL = "https://www.s-vfu.ru"
INSTITUTES_URL = "https://www.s-vfu.ru/universitet/rukovodstvo-i-struktura/instituty/"
STAFF_URL = "https://www.s-vfu.ru/staff/{}"
SCHEDULE_URL = "https://www.s-vfu.ru/raspisanie/ajax.php"

Prepod = namedtuple("Prepod", ["name", "phone", "mail", "img_url", "address"])
Subject = namedtuple("Subject", ["day", "time", "group", "name", "audience"])
Schedule = namedtuple("Schedule", ["subjects"])
Day = namedtuple("Day", ["day", "date", "pairs"])
Pair = namedtuple("Pair", ["time", "name", "prepod", "audience"])
Schedule2 = namedtuple("Schedule2", ["days"])


def get_institute_staff_urls():
    html = requests.get(INSTITUTES_URL).content

    soup = BeautifulSoup(html)

    institute_staff_urls = set()

    for td in soup.find_all("td"):
        for a in td.find_all("a"):
            url = "https://www.s-vfu.ru" + (a.attrs['href'] + '/staff/').replace("//", "/")
            institute_staff_urls.add(url)

    return institute_staff_urls


def get_staff_ids():
    staff_ids = set()

    for url in constants.institute_staff_urls:
        html = requests.get(url).content
        soup = BeautifulSoup(html)
        for h4 in soup.find_all("h4"):
            for a in h4.find_all("a"):
                staff_ids.add(a.attrs["href"].split("/")[-1])

    return staff_ids


def get_prepod_schedule(id):
    data = {"mydate": datetime.datetime.today().strftime('%d-%m-%Y'), "prepid": id, "action": "showprep"}
    soup = BeautifulSoup(requests.post(SCHEDULE_URL, data).content.decode('utf-8'))
    subjects = []
    for tr in soup.find_all("tr", class_="success"):
        tds = tr.find_all("td")
        day = tds[0].text.strip()
        time = tds[1].text
        group = tds[2].find("a").text
        name = tds[3].text
        audience = tds[4].find("a").text
        subject = Subject(day, time, group, name, audience)
        subjects.append(subject._asdict())
    schedule = Schedule(subjects)
    return json.dumps(schedule._asdict(), ensure_ascii=False)


def get_prepod_info(id):
    url = STAFF_URL.format(id)
    html = requests.get(url).content
    soup = BeautifulSoup(html).find("div", class_="right_colum")
    name = soup.find("h1").text.strip()
    phone = soup.find("div").find_all("p")[0].text.strip()
    mail = soup.find("div").find_all("p")[2].text.strip()
    address = soup.find("div").find_all("p")[3].text.strip()
    img_url = SVFU_URL + soup.find("div").find("img").attrs["src"]
    prepod = Prepod(name, phone, mail, address, img_url)
    print(prepod)


def get_schedule2(group_name):
    data = {"mydate": datetime.datetime.today().strftime('%d-%m-%Y'), "groupname": group_name, "action": "showrasp"}
    soup = BeautifulSoup(requests.post(SCHEDULE_URL, data).content.decode('utf-8')).find("tbody")
    day_name = ""
    pairs = []
    days = []
    date = ""
    for tr in soup.find_all("tr"):
        if tr.attrs["class"] == ["error"]:
            if len(pairs) > 0:
                days.append(Day(day_name, date, pairs)._asdict())
                pairs = []
            day_name = tr.text.split()[0]
            date = " ".join(tr.text.split()[1:])
        else:
            tds = tr.find_all("td")
            time = tds[0].text
            name = tds[1].text
            prepod = tds[2].text
            audience = tds[3].find("a").text
            pair = Pair(time, name, prepod, audience)
            pairs.append(pair._asdict())

    days.append(Day(day_name, date, pairs)._asdict())
    schedule2 = Schedule2(days)
    return json.dumps(schedule2._asdict(), ensure_ascii=False)

#
#
# return json.dumps(schedule._asdict(), ensure_ascii=False)
