FROM python:3
RUN pip install -U pip
RUN pip install --no-cache-dir tensorflow bert-serving-server
COPY ./ /app
COPY ./entrypoint.sh /app
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []