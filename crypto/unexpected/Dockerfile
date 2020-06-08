FROM python:3


RUN apt-get update -qq && \
apt-get install -y --no-install-recommends \
libmpc-dev \
libgmp-dev \
libmpfr-dev

RUN pip install gmpy2 pycryptodome

ADD solution.py /
