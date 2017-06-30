#!/bin/sh
uwsgi --gevent 2 --http :8000 --wsgi-file app.py --callable app --static-map /suchsecret=jars
