FROM python:latest
WORKDIR /etl
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-u", "code/run_etl.py"]
# CMD ["sleep", "infinity"]