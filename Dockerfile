FROM python:3.10.2-alpine3.15

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]