FROM python:3.6-stretch
ADD . /backend
RUN pip install -r requirements.txt
CMD ["python", "."]