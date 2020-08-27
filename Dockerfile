FROM python:3.8.3-alpine

RUN pip install pipenv
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "api/api.py"]
