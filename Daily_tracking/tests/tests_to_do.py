import pytest
from app.utils import add_task, remove_task

def test_add_task():
    tasks = []
    add_task(tasks, "Test Task")
    assert tasks == ["Test Task"]

def test_remove_task_valid():
    tasks = ["Task 1", "Task 2"]
    assert remove_task(tasks, 1) == True
    assert tasks == ["Task 2"]

def test_remove_task_invalid():
    tasks = ["Task 1"]
    assert remove_task(tasks, 5) == False
    assert tasks == ["Task 1"]
