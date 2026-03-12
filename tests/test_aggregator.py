import pytest

from src.aggregator import Aggregator
from src.source import GeneratorSource
from src.task import Task


def test_aggregator():
    aggregator = Aggregator()
    aggregator.bind_source(GeneratorSource())
    tasks = aggregator.aggregate_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == "generated_1"
    aggregator.run()


def test_empty_aggregator():
    aggregator = Aggregator()
    aggregator.run()


def test_incorrect_payload():
    aggregator = Aggregator()
    incorrect_payload_task = Task(
        id="test_1",
        payload=67
    )
    with pytest.raises(RuntimeError):
        aggregator.handle_task(incorrect_payload_task)
