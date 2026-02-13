FROM python:3.13.11-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#EXPOSE 5000
ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0
#ENV FLASK_RUN_PORT=5000
CMD ["flask", "run"]