FROM python:3.7

WORKDIR /usr/src/app

ADD . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r  plist.txt

RUN  python manage.py migrate

EXPOSE 80:80

