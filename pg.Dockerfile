FROM postgres:15
WORKDIR /sql_scripts
COPY sql_init_scripts/create_tables.sql \
sql_init_scripts/insert_data.sql \
sql_init_scripts/create_triggers.sql \
/docker-entrypoint-initdb.d/
COPY /sql_scripts /sql_scripts
