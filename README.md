# ruby-docker

## Build

```bash
docker build -t smathewthomas/python:3.8.13-alpine3.16  .
```

## Run

```bash
docker run --rm -ti -p 3000:3000  -v "$(pwd)":/app smathewthomas/python:3.8.13-alpine3.16 /bin/bash
```