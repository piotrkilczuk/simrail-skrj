FROM ubuntu

RUN apt update && apt install -y build-essential default-jre libreoffice

WORKDIR /workdir

CMD make
