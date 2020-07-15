FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

RUN curl -sL https://deb.nodesource.com/setup_13.x | bash -
RUN apt-get install -y nodejs

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN cd /code/frontend 

RUN npm install
RUN npm run build

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]