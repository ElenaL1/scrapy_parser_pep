# scrapy_parser_pep

### Реализован парсер документов PEP на базе фреймворка Scrapy с сайта https://www.python.org/dev/peps/

Парсер выводит собранную информацию в два файла .csv в папку results:
- В первый файл выводится список всех PEP: номер, название и статус (файл pep_ДатаВремя.csv).
- Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке указывается общее количество всех документов. (файл status_summary_ДатаВремя.csv)


### Запуск парсера
Клонируйте репозиторий к себе на компьютер. Создайте виртуальное окружение и установите зависимости из файла requirements.txt. 
Парсер запускается командой из корневого каталога:
`scrapy crawl pep`
