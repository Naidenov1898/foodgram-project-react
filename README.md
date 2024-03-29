# praktikum_new_diplom
![foodgram](https://github.com/Naidenov1898/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

## Сайт

Проект доступен по ссылке: [Foodgram](http://158.160.50.59/)


# Foodgram - «Продуктовый помощник»

Пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд

# Системные требования
- выделенный linux Ubuntu сервер
- внешний IP адрес
- зарегистрировнное доменное имя
- nginx 
- docker
- docker compose

# Установка
Подготовьте сервер к установке

Клонируйте репозиторий<br/>
в каталоге /infra/ Создайте .env файл в формате<br/>
<br/>
SECRET_KEY=Ah!Is3g|&~fftth4e3sssqq["$8(A$]<:&&<br/>
DB_ENGINE=django.db.backends.postgresql<br/>
DB_NAME=postgres<br/>
POSTGRES_USER=postgres<br/>
POSTGRES_PASSWORD=postgres<br/>
DB_HOST=db<br/>
DB_PORT=5432<br/>

<br/>
скопируйте папку /infra/<br/>
scp -r infra/* di@<you server ip>:/home/< username >/foodgram/<br/>
<br/>
подключитесь к серверу через ssh и перейдите в каталог<br/>
/home/< username >/foodgram/<br/>
<br/>
запустите установку и сборку контейнеров<br/>
docker compose up -d<br/>

## Полезные команды при работе с Docker
посмотреть логи контейнера<br/>
docker logs --since=1h <container_id><br/>

подключить к контейнеру<br/>
docker exec -it  sh<br/>

### список контейнеров, образов, и volumes
docker ps<br/>
docker image ls<br/>
docker volume ls<br/>

остановить все контейнеры и удалить
docker compose stop<br/>
sudo docker compose rm web<br/>
docker stop $(docker ps -a -q)<br/>
docker rm $(docker ps -a -q)<br/>
docker rmi $(docker image ls)<br/>

# Создайте суперпользователя
Создайте администратора как в обычном Django-проекте<br/>
docker ps<br/>
docker exec -it < CONTAINER ID > bash <br/>

python manage.py createsuperuser<br/>

теперь вы можете работать с админ панелью<br/>
<you server name>/admin/<br/>

# Логин и пароль
admin
admin

# Автор backend сервисов
[Найденов Константин](https://github.com/Naidenov1898)
