#!/bin/bash


postgres_host=$DB_SERVICE
postgres_port=$DB_PORT
shift 2
cmd="$@"

# wait for the postgres docker to be running
while ! nc $postgres_host $postgres_port; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up - executing command"


python manage.py migrate

python manage.py generate_test_data

python manage.py create_auth_tokens