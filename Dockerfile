FROM python:3.11.8-alpine3.19
LABEL maintainer="KajalYadav"

ENV PYTHONUNBUFFERED 1

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir /SocialDj
WORKDIR /SocialDj
COPY ./requirements.txt /tmp/requirements.txt
COPY . /SocialDj/
EXPOSE 8000

RUN python -m venv /py && \
    source /py/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"

USER django-user