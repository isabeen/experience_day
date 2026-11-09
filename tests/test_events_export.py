from uuid import UUID
from datetime import datetime
import requests


def get_export_url(base_url, customer_id):
    return f"{base_url}/{customer_id}/events/export/tasks"


def test_create_events_export_task(session, base_url, customer_id):
    """
    POST /{customer_id}/events/export/tasks
    Verify successful creation of an Events Export task.
    """
    response = session.post(
        get_export_url(base_url, customer_id),
        json={}
    )
    assert response.status_code == 202

    data = response.json()
    print("Response JSON:", data)

    assert "task" in data
    assert isinstance(data["task"], str)
    UUID(data["task"])

    assert "requested" in data
    assert isinstance(data["requested"], str)
    datetime.fromisoformat(data["requested"])


def test_events_export_unauthorized(base_url, customer_id):
    """
    POST /{customer_id}/events/export/tasks
    Verify that export requests without authentication are rejected.
    """
    response = requests.post(
        get_export_url(base_url, customer_id),
        json={}
    )
    assert response.status_code == 401
    print("Response JSON:", response.json())
