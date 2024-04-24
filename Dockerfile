FROM python:3.11.8-alpine3.19
LABEL maintainer="KajalYadav"

ENV PYTHONUNBUFFERED 1

RUN mkdir /SocialDj
WORKDIR /SocialDj
COPY ./requirements.txt /tmp/requirements.txt
COPY . /SocialDj/
EXPOSE 8000


ENV PATH="/py/bin:$PATH"

USER django-user