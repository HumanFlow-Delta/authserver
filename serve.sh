#!/usr/bin/env fish

set SECRET_KEY MmY5YWU5YzdhYzY3MWJkYWI3YjZkNjBh
set FLASK_ENV development
set DATABASE_URL db/test.sqlite

flask run --reload --eager-loading --without-threads --port 8080 --host 0.0.0.0
