FROM python:3
MAINTAINER shen.charles@hotmail.com
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
COPY . .
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "simplesurvey.wsgi"]