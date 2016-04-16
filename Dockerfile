FROM python:2.7

COPY hitcounter.py .
RUN pip install flask redis

CMD python hitcounter.py

EXPOSE 80
