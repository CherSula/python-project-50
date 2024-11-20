# Данная программа - "Вычислитель отличий", создана для сравнения двух файлов с данными

### Hexlet tests and linter status:
[![Actions Status](https://github.com/CherSula/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/CherSula/python-project-50/actions)
### CodeClimate:
[![Maintainability](https://api.codeclimate.com/v1/badges/22eaee8f1739869c2d9e/maintainability)](https://codeclimate.com/github/CherSula/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/22eaee8f1739869c2d9e/test_coverage)](https://codeclimate.com/github/CherSula/python-project-50/test_coverage)

## О проекте
Программа создана в качестве проекта для прохождения обучения и получения практического опыта разработки на языке Python на курсе компании __Хекслет__.
Она сравнивает два файла, принимая на вход через командную строку два аргумента — пути до этих файлов.
Результат сравнения файлов выводится в одном из заданных форматов: plain ("плоский"), stylish (стильный) или json ("JSON-формат"). 

---
## Требования
###### Для установки и запуска проекта, необходимы:
~~~sh
1. python версии 3.10 и выше
2. pyyaml = "^6.0.1" и выше
3. poetry версии 1.6.1 и выше
~~~

## Установка
##### 1. установите менеджер пакетов **poetry**(https://python-poetry.org/docs/)

##### 2. создайте виртуальное окружение в директории проекта
~~~
$ # выполните команду
poetry config virtualenvs.in-project true
~~~
##### 3. склонируйте репозиторий проекта

##### 4. подключите в зависимости библиотеку **pyyaml**
```
poetry add pyyaml
```
##### 5. собирите проект
```
make build
```

##### 6. установите проект
```
make package-install
```

## Запуск программы
 
* без опции --format
```
**poetry** run **gendiff** [path to file]**file1.json** [path to file]**file2.json**
**poetry** run **gendiff** [path to file]**file1.yml** [path to file]**file2.yml**
```
* для вывода в нужном формате:
```
poetry run gendiff --format stylish [path to file]**file1.yml** [path to file]**file2.yml**
poetry run gendiff --format plain [path to file]**file1.yml** [path to file]**file2.yml**
poetry run gendiff --format json [path to file]**file1.yml** [path to file]**file2.yml**
poetry run gendiff --format stylish [path to file]**file1.json** [path to file]**file2.json**
poetry run gendiff --format plain [path to file]**file1.json** [path to file]**file2.json**
poetry run gendiff --format json [path to file]**file1.json** [path to file]**file2.json**
```

## Пример работы программы
[![asciicast](https://asciinema.org/a/689968.svg)](https://asciinema.org/a/689968)

#### GitHub Workflows:
[![Hexlet-check](.github/workflows/hexlet-check.yml)](https://github.com/CherSula/python-project-50/blob/62d57322b9d7bcaaa7546f1d83fdf3170c9d38a9/.github/workflows/hexlet-check.yml)
[![Pylint](.github/workflows/pylint.yml)](https://github.com/CherSula/python-project-50/blob/62d57322b9d7bcaaa7546f1d83fdf3170c9d38a9/.github/workflows/pylint.yml)
