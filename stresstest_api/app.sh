#!bash
uwsgi -s /tmp/uwsgi.sock -w app:app -H ../ --chmod-socket=666
