#!/bin/bash
#!/bin/sh

python manage.py runserver 0.0.0.0:8000
exec "$@"