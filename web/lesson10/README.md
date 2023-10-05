1. Start MongoDB docker-container:

`docker run --name WEBHW10 -p 27017:27017 -d mongo`

2. Manualy import `authors.json` to mongoDB.
3. Run `add_quotes_to_mongo.py` to download quotes data in MongoDB.
4. After applying migrations in Django for the Postgres database, run `custom_migration.py` to download all data in Postgres.
