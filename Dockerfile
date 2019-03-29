FROM python:3.6-stretch
ADD . /svfu-assistant
WORKDIR /svfu-assistant
RUN pip install -r requirements.txt
CMD ["python", "."]