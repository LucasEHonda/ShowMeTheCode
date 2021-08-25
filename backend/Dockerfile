FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

RUN cat manage.py
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]