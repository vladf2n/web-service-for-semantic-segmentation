FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install libgtk2.0-dev -y
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python ./run.py