FROM mongo

COPY file.json /file.json

#ADD start.sh /start.sh
#RUN chmod +x /start.sh

CMD mongoimport --host mongodb --db articles --collection articles_collection --type json --file /file.json --jsonArray