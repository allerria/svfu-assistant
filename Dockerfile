FROM python:3.6-stretch
RUN pip install -r requirements.txt
CMD ["python", "."]