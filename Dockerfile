FROM python:3.8-slim

WORKDIR /app/

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./cnab_reader/ /app/cnab_reader/

COPY ./_desafiobackend/ /app/_desafiobackend/

COPY manage.py /app/

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]