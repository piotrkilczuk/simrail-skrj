FROM ubuntu

RUN apt update && apt install -y build-essential default-jre libreoffice python3 python-is-python3
RUN useradd --create-home skrj
ADD resources/fonts /usr/share/fonts/opentype
RUN fc-cache -f -v

WORKDIR /workdir
USER skrj
ENV PYTHONPATH=/workdir/src

CMD make
