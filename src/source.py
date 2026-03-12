from src.task import Task
from typing import Protocol, runtime_checkable

from random import randint
from pathlib import Path
import json
from time import sleep


@runtime_checkable
class Source(Protocol):
    """
    Протокол источника
    """

    def get_tasks(self) -> list[Task]:
        """
        Метод, который возращает задачи
        :return: Список задач
        """
        ...


class GeneratorSource(Source):
    """
    Источник задач. Генератор
    """

    def __init__(self):
        self.count = 0

    def get_tasks(self) -> list[Task]:
        self.count += 1

        return [
            Task(
                id=f"generated_{self.count}",
                payload=f"generated payload {randint(1, 10)}"
            )
        ]


class JsonSource(Source):
    """
    Источник задач. Из Json файла
    """

    def __init__(self, file: str):
        self.file = Path(file)
        if not self.file.exists():
            raise NameError("Файл не существует")

    def get_tasks(self) -> list[Task]:
        with open(self.file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise ValueError(f"Не получилось загрузить Json: {e}")

        return [
            Task(
                id=task["id"],
                payload=task["payload"]
            )
            for task in data
        ]


class ApiSource(Source):
    """
    Источник задач. Api заглушка
    """

    def __init__(self, fake_requests: int):
        self.count = 0
        self.fake_requests = fake_requests

    def get_tasks(self) -> list[Task]:
        tasks: list[Task] = []
        for i in range(self.fake_requests):
            self.count += 1
            sleep(randint(1, 3))
            tasks.append(
                Task(
                    id=f"api_{self.count}",
                    payload=f"api payload #{i}"
                )
            )
        return tasks
