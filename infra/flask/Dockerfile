FROM python:alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask
EXPOSE 5000
CMD ["flask", "run"]