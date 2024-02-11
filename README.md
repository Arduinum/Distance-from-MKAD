# Distance-from-MKAD
Distance from MKAD - приложение для измерения расстояния от МКАД до указанного адреса.

Данные вернёт в .log (str) файл и на экран браузера (json)

## Стек

- Python 3.8.0 - версия питона
- Flask 3.0.2 - фреймворк
- requests 2.31.0 - библиотека для запросов

## Установка версии python и настройка виртуального окружения

Я использую pyenv, но вы можете настроить окружение любым удобным вам способом.

Инструкция по установке (для других ОС)
https://github.com/pyenv/pyenv?tab=readme-ov-file#installation

Пример настройки на Linux Kubuntu

curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

nano ~/.bash_profile

export PATH="/home/USER/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.8.0

pyenv virtualenv 3.8.0 name_venv

source ~/.bash_profile
pyenv shell name_venv

## Установка и прверка библиотек 

pip install -r requirements.txt

pip freeze

## Если есть проблемы с импортом в unit-тестах

Запустите из главного каталога
export PYTHONPATH=$PWD

## Пример запуска приложения

Cоздайте файл .env в главном каталоге проекта скопировав содержимое .env.example

Запуск из terminal linux

export FLASK_ENV=development

flask run --host=127.0.1.1 --port=5001 --debug

Простейший пример запуска (обязательно выбрать интерпретатор из виртуального окружения!)

1. IDE -> app.py -> run/запустить код (В моём примере приложение стартует с debug=True и host='127.0.1.1')
2. Перейдите в браузер (в моём случае это Firefox)
3. Пример корректного запроса:
   http://127.0.1.1:5000/geo_data?target=Нижний%20Новгород
4. Пример запроса с мкад (должна быть ошибка та как в пределах мкад)
   http://127.0.1.1:5000/geo_data?target=МКАД%2C%71-й%20километр%2C%Москва

Примечание к запросу: %2C% это ", " и %20 - " "

## Пример запуска тестов

Запуск из terminal linux

cd tests

python test_views.py

Простейший пример запуска (обязательно выбрать интерпретатор из виртуального окружения!)

IDE -> tests/test_views.py -> run/запустить код

## .log файл

.log создаётся по адресу logger/.log
