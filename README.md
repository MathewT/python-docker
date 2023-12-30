# python-docker

## Build

```bash
docker build -t smathewthomas/python:3.12.1-alpine3.19  .
```

## Run

```bash
docker run --rm -ti -p 3000:3000  -v "$(pwd)":/app smathewthomas/python:3.12.1-alpine3.19 /bin/bash
```

## Useful links

[AWS Lambda Function Logging](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html)

