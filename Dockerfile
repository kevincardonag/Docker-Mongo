FROM python:3

COPY convert-csv.py /
COPY scopus2017.csv /
COPY scopus2018.csv /
COPY scopus2019.csv /

RUN python3 convert-csv.py
EXPOSE 9000

CMD ["/bin/bash"]