FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN apt-get update

RUN apt-get install -y fortune-mod cowsay netcat-openbsd

RUN chmod +x wisecow.sh

# Alot of brainstorming then got the solution
ENV PATH="/usr/games:${PATH}"

EXPOSE 4499

CMD ["/app/wisecow.sh"]
