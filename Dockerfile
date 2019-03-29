FROM python:3.6-stretch
ADD . .
WORKDIR .
RUN pip install -r requirements.txt
CMD ["python", "."]