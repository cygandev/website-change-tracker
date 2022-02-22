FROM python:3.10.2-alpine3.15

ARG EMAIL_RECEIVER
ARG PW_GMAIL
ARG EMAIL
ARG URL

COPY . .

RUN pip install -r requirements.txt

RUN crontab crontab

CMD ["crond", "-f"]