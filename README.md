# eduplatform
"General educational project"

Для настройки базы данных необходимо войти в контейнер "eduplatform_db" командой:

$ docker exec -it [id image] bash

После входа в консоль контейнера команда для входа в консоль постгрес:

$ psql -U postgres -d postgres

Создать базу данных:

$ CREATE DATABASE eduplatform_postgres_db;

Создать пользователя:

$ CREATE USER eduplatform_web WITH LOGIN PASSWORD '1111';

Добавить права доступа пользователя к бд:

$ GRANT ALL PRIVILEGES ON DATABASE eduplatform_postgres_db TO eduplatform_web;

Добавить права пользователю для создания бд(нужно для тестов), просто для работы этого не нужно

$ alter user eduplatform_web superuser createdb;
