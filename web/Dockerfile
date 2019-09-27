FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -U pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]