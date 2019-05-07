FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

ADD app/requirements.prod.txt /app/requirements.prod.txt
RUN pip install -r /app/requirements.prod.txt \
	--index-url http://mirrors.aliyun.com/pypi/simple/ \
	--trusted-host mirrors.aliyun.com

ADD app/ /app/
WORKDIR /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
