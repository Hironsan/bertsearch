FROM python:3.8.6-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENTRYPOINT ["python"]
CMD ["app.py"]
