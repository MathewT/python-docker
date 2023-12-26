# FROM python:3.8.13-alpine3.16
# FROM python:3.9.13-alpine3.16
FROM python:3.12.1-alpine3.19

RUN apk add --update build-base bash bash-completion libffi-dev tzdata git postgresql-client postgresql-dev

WORKDIR /app

RUN mkdir $HOME/.ssh
RUN touch $HOME/.bashrc

RUN echo "alias ll='ls -alF'" >> $HOME/.bashrc
RUN echo "alias la='ls -A'" >> $HOME/.bashrc
RUN echo "alias l='ls -CF'" >> $HOME/.bashrc
RUN echo "alias q='exit'" >> $HOME/.bashrc
RUN echo "alias c='clear'" >> $HOME/.bashrc


CMD [ "bash" ]

