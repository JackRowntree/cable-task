FROM python:latest
WORKDIR /etl
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["/bin/bash", "run_end_to_end.sh"]
# CMD ["sleep", "infinity"]