### Hi there 👋, Dmitrii
#### Асинхронный парсер документации PEP


+ Парсер документации PEP на базе фреймворка Scrapy. 
+ Парсер собирает информацию со страницы https://peps.python.org/
+ Парсер выводит собранную информацию в два файла .csv:

в первом список всех PEP: номер, название и статус.
второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество).

+ Используемые технологии: Python / Scrapy
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/xrito/scrapy_parser_pep
```
```
cd scrapy_parser_pep
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

## Запуск парсера командой:

`scrapy crawl pep`

[<img src='https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg' alt='github' height='40'>](https://github.com/xrito)  

