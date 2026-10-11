"""Visible logic tests for the to-do API. They must pass on the clean app."""

import pytest
from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_app():
    """Start every test with an empty task list."""
    main.tasks.clear()
    main.next_id = 1


def add(title: str) -> dict:
    """Add a task through the API and return it."""
    response = client.post("/tasks", json={"title": title})
    assert response.status_code == 201
    return response.json()


def test_add_task_appears_in_list_not_completed():
    task = add("Buy milk")

    assert task["title"] == "Buy milk"
    assert task["completed"] is False
    assert client.get("/tasks").json() == [task]


def test_tasks_get_unique_ids():
    first = add("One")
    second = add("Two")

    assert first["id"] != second["id"]


def test_complete_changes_only_that_task():
    first = add("One")
    second = add("Two")

    response = client.patch(f"/tasks/{second['id']}/complete")

    assert response.status_code == 200
    by_id = {t["id"]: t for t in client.get("/tasks").json()}
    assert by_id[second["id"]]["completed"] is True
    assert by_id[first["id"]]["completed"] is False


def test_delete_removes_only_the_given_task():
    first = add("One")
    second = add("Two")
    third = add("Three")

    response = client.delete(f"/tasks/{second['id']}")

    assert response.status_code == 200
    remaining_ids = [t["id"] for t in client.get("/tasks").json()]
    assert remaining_ids == [first["id"], third["id"]]


@pytest.mark.parametrize("title", ["", "   "])
def test_empty_or_whitespace_title_is_rejected(title):
    response = client.post("/tasks", json={"title": title})

    assert response.status_code == 400
    assert client.get("/tasks").json() == []


def test_complete_unknown_task_returns_404():
    assert client.patch("/tasks/999/complete").status_code == 404


def test_delete_unknown_task_returns_404():
    assert client.delete("/tasks/999").status_code == 404
