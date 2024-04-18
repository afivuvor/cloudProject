FROM python:3.12.0

ENV PYTHONUNBUFFERED True

ENV APP_HOME /back-end

WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app