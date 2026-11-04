FROM python:3.14-alpine

ENV FLASK_APP=/app/main.py
ENV MY_VAR='Moja zmianna środowiskowa'
RUN pip install --no-cache-dir Flask==3.1.3

WORKDIR /app

COPY main.py /app

EXPOSE 9085

ENTRYPOINT ["python"]
CMD ["main.py"]


