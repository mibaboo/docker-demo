FROM python:alpine
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY src/ .

RUN pip install --ignore-installed -r requirements.txt

EXPOSE 8080
CMD ["python" ,"/usr/src/app/main.py"]
