FROM alpine
RUN apk add --update python3 py-pip
COPY NewsApp.py NewsQueue.py /app/
WORKDIR /app
CMD ["python", "NewsApp.py"]