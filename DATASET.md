# Dataset Guide

Техническое описание распакованного корпуса из папки [`translation_record/`](translation_record/).

## Коротко

Датасет хранится в SQLite-базах, созданных в процессе извлечения и перевода текста **Summer Pockets Reflection Blue**. Главный файл с корпусом находится в корне папки `translation_record/`, а дополнительные кеши переводчиков вынесены в `translation_record/cache/`.

Архив [`translation_record.7z`](translation_record.7z) оставлен как компактная копия тех же данных.

## Основные файлы

| Файл | Назначение | Примерный объем |
| --- | --- | --- |
| `translation_record/SummerPocketsRB_1771957083.197056_c0538fba-7b9a-4ac0-b0a6-511637015b17.sqlite` | Основная база корпуса | 58 348 строк в `artificialtrans` |
| `translation_record/0_ocr.sqlite` | OCR-слой для текста, который не удалось стабильно получить хуком | 8 016 строк в `artificialtrans` |
| `translation_record/0_copy.sqlite` | Небольшая вспомогательная база | 2 строки в `artificialtrans` |
| `translation_record/script.py` | Скрипт для базовой статистики по основной базе | считает строки и длину исходного текста |
| `translation_record.7z` | Сжатая копия папки `translation_record/` | удобно скачать одним файлом |

## Кеши переводчиков

| Файл | Содержимое |
| --- | --- |
| `translation_record/cache/chatgpt-3rd-party.sqlite` | кеш запросов к ChatGPT-compatible переводчику |
| `translation_record/cache/deepl_1.sqlite` | кеш DeepL |
| `translation_record/cache/google.sqlite` | кеш Google Translate |
| `translation_record/cache/yandex.sqlite` | кеш Yandex Translate |
| `translation_record/cache/yandexapi.sqlite` | кеш Yandex API |
| `translation_record/cache/TranslateCom.sqlite` | кеш Translate.com |
| `translation_record/cache/papago.sqlite` | кеш Papago |

Часть вспомогательных баз может быть пустой. Они сохранены для прозрачности происхождения данных и повторяемости структуры.

## Формат данных

Основные базы используют таблицу `artificialtrans`. В ней находятся исходные строки и связанные с ними варианты автоматического перевода. Точную схему лучше смотреть напрямую через SQLite-клиент, потому что разные источники и кеши могут отличаться набором полей.

Пример просмотра схемы:

```bash
sqlite3 translation_record/SummerPocketsRB_1771957083.197056_c0538fba-7b9a-4ac0-b0a6-511637015b17.sqlite ".schema artificialtrans"
```

Пример подсчета строк:

```bash
sqlite3 translation_record/SummerPocketsRB_1771957083.197056_c0538fba-7b9a-4ac0-b0a6-511637015b17.sqlite "select count(*) from artificialtrans;"
```

## Быстрая проверка через Python

```bash
python translation_record/script.py
```

Скрипт считает количество строк, общий объем символов и несколько базовых статистик по колонке `source` в основной базе.

## Важные ограничения

- Корпус не является полной официальной выгрузкой игры.
- Рута Уми отсутствует.
- Скрытые диалоги могут быть неполными.
- OCR-строки могут содержать ошибки распознавания.
- Машинный перевод не проходил полную ручную вычитку.
