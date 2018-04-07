 FROM python:3
 ENV PORT 5000
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 COPY requirements.txt /code/
 RUN pip -r install requirements.txt
 ADD . /code/
 CMD python3 manage.py runserver 0.0.0.0:$PORT
 # CMD gunicorn -b 0.0.0.0:$PORT --log-file -
 #ENTRYPOINT [ "executable" ]
