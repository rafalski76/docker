FROM python:3.6-alpine

ENV FLASK_APP=/main.py
ENV MY_VAR='Moja zmianna środowiskowa' 
RUN pip install Flask==1.0.2

WORKDIR /app

COPY main.py /app

EXPOSE 9085 

ENTRYPOINT ["python"]
CMD ["main.py"] 


