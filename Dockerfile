FROM alpine:3.6

ENV PYTHONBUFFERED 1

ARG APP_PATH=/warp

RUN apk --update add python3 python3-dev build-base linux-headers libxml2-dev libxslt-dev

COPY requirements.txt $APP_PATH/requirements.txt
RUN pip3 install -r $APP_PATH/requirements.txt

COPY . $APP_PATH

WORKDIR $APP_PATH

CMD ["./run.sh"]

