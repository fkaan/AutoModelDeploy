FROM ubuntu:latest
LABEL authors="fekef"

ENTRYPOINT ["top", "-b"]