FROM python
COPY . ./myblog
USER root
EXPOSE 8000

RUN apt-get update
RUN pip install -r requirements.txt
# CMD = ["python ", "manage.py ", "runserver ", " 0.0.0.0:8000"]
