FROM python:3.8-slim-buster
WORKDIR /usr/src/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#erver will reload itself on file changes if in dev mode
ENV FLASK_ENV=development 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
COPY companyblog companyblog
COPY migrations migrations
COPY model model
CMD ["flask", "run","--host=0.0.0.0"]
