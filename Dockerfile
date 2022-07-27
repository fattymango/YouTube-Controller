FROM selenium/standalone-chrome
USER root
RUN apt-get update && apt-get install -y python3.9 python3.9-dev

RUN set -xe \
    && apt-get update \
    && apt-get install -y python3-pip

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . /app
WORKDIR /app

# FROM selenium/standalone-chrome
# USER root
# RUN apt-get update && apt-get install -y python3.9 python3.9-dev

# RUN set -xe \
#     && apt-get update \
#     && apt-get install -y python3-pip \ 
#     && apt-get install -y git

# RUN git clone https://github.com/FattyMango/YouTube-Controller
# RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install -r requirements.txt



# WORKDIR /YouTube-Controller

