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
воспользуйтесь [дополнительными рекомендациями по установке сервера]()<br/>
<br/>
Клонируйте репозиторий<br/>
в каталоге /infra/ Создайте .env файл в формате<br/>
<br/>
DEBUG=False<br/>
SECRET_KEY=Ah!Is3g|&~fftth4e3sssqq["$8(A$]<:&&<br/>
ALLOWED_HOSTS=127.0.0.1 10.0.1.100 localhost web foodgram.auxlink.com 95.165.26.109 backend<br/>
CSRF_TRUSTED_ORIGINS = http://localhost http://127.0.0.1 https://foodgram.auxlink.com<br/>
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


# Автор backend сервисов
[Найденов Константин]()


