# Building
Build and run:

docker-compose up 

# para entrar en el root del contenedor 

docker exec -it django_container bash

# para ejecutar migraciones de models y demas 

python manage.py make migrations

python manage.py migrate
