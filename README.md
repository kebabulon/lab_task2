# Лаба 1: Источники задач и контракты

## Запуск
```bash
uv venv
uv sync
source .venv/bin/activate
# для винды: .venv\Scripts\activate

# запуск
python -m src.main

# тестирование
pytest
```

## Принятые решения
- Задача `Task`. Простой dataclass с `id` и `payload`
- Контракт `Source`. Протокол который задает метод `get_tasks(): -> list[Task]`
- Три источника задач, которые соблюдают контракт `Source`:
    * `GeneratorSource` - программная генерация задач
    * `JsonSource` - загруска задач из JSON файла
    * `ApiSource` - API-заглушка, имитирует совершение запросов используя `time.sleep()`
- Класс `Aggregator`. Позволяет добавить источники, собирать задачи от этих источников и обрабатывать задачи.
- Проверяет соблюдение контракта источниками и тип `payload` через `isinstance()`
- Логирование соблюдается в `Aggregator`
