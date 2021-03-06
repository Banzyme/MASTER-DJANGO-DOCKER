 FROM python:3
 ENV PORT 5001
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 COPY requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD . /code/
 #CMD python3 manage.py runserver 0.0.0.0:$PORT
 CMD python3 manage.py makemigrations &&\
     python3 manage.py migrate &&\
     gunicorn twisted.wsgi -b 0.0.0.0:$PORT --log-file -
 #ENTRYPOINT [ "executable" ]
