#!/bin/bash

python manage.py migrate

python manage.py generate_test_data

python manage.py create_auth_tokens