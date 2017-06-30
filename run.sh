#!/bin/sh
uwsgi --gevent 100 --http :8000 --wsgi-file app.py --callable app --static-map /suchsecret=jars
