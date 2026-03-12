import pytest

from src.task import Task, StatusEnum
from datetime import datetime


def test_task():
    # priority
    with pytest.raises(ValueError):
        _ = Task(
            id=1,
            payload="test",
            priority=-1
        )
    task = Task(
        id=1,
        payload="test",
    )
    task.priority = 5
    with pytest.raises(ValueError):
        task.priority = -1

    # time_created non-data descriptor
    with pytest.raises(AttributeError):
        task.time_created = datetime.now()

    # status
    task.status = StatusEnum.PROCESSING
    with pytest.raises(ValueError):
        task.status = StatusEnum.NOT_STARTED
    task.status = StatusEnum.COMPLETED
    with pytest.raises(ValueError):
        task.status = StatusEnum.PROCESSING
