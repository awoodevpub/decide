psql -c "create user decide with password 'decide'"
psql -c "create database decide owner decide"
python manage.py makemigrations
python manage.py migrate