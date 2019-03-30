FROM python:3.6-stretch
ADD . .
# install gcc and g++ so that liblpclassifier_cv32 can utilize the library
RUN echo 'deb http://deb.debian.org/debian/ sid main' >> /etc/apt/sources.list
RUN apt-get update -y && \
    apt-get install -y \
      gcc-5 \
      g++-5 && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get remove -y cmake
RUN curl -O https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.sh
RUN sh cmake-3.8.2-Linux-x86_64.sh --skip-license
RUN pip install -r requirements.txt
CMD ["python", "./__main__.py"]