FROM  python:3.6-slim 
MAINTAINER Antonio Royo "antonio.royo@outlook.com"
RUN apt-get update -y
RUN apt-get install -y python3-dev build-essential \
    libxft-dev libfreetype6 libfreetype6-dev 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["apptoni.py"]
