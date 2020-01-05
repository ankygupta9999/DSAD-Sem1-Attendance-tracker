FROM python:3.6.3
USER root

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN mkdir -p /app/plots
RUN pip install -r /app/requirements.txt

EXPOSE 5000
RUN chown -R 1001:0 /app/ && \
    chmod -R g+wrx /app/
USER 1001

CMD python /app/cherrreporting/cherrreporting.py
