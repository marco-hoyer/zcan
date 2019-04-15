FROM arm64v8/alpine:3.8

RUN apk update && apk add python3 python3-dev musl-dev linux-headers gcc
RUN pip3 install pybuilder

COPY . .
RUN pyb install_dependencies
RUN pyb install

ENTRYPOINT ["zcan", "run"]
