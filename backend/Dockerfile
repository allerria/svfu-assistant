FROM python:3.6-stretch
ADD . .
# install gcc and g++ so that liblpclassifier_cv32 can utilize the library
RUN pip install -r requirements.txt
CMD ["python", "./__main__.py"]