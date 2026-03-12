from dataclasses import dataclass


@dataclass
class Task():
    """
    Класс задачи
    """
    id: str
    payload: object
