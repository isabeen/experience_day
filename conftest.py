import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("INSIGHT_BASE_URL")


@pytest.fixture(scope="session")
def customer_id():
    return os.getenv("CUSTOMER_ID")


@pytest.fixture(scope="session")
def token(base_url, customer_id):

    # Step 1: Get authentication information
    response = requests.get(
        f"{base_url}/auth-information",
        params={"id": customer_id}
    )
    assert response.status_code == 200
    auth_info = response.json()

    region = auth_info["region"]
    client_id = auth_info["user_pool_client_id"]

    # Step 2: Authenticate with AWS Cognito
    login_url = f"https://cognito-idp.{region}.amazonaws.com/login"
    headers = {
        "Content-Type": "application/x-amz-json-1.1",
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth"
    }
    payload = {
        "AuthFlow": "USER_PASSWORD_AUTH",
        "ClientId": client_id,
        "AuthParameters": {
            "USERNAME": os.getenv("INSIGHT_USERNAME"),
            "PASSWORD": os.getenv("INSIGHT_PASSWORD")
        }
    }
    response = requests.post(
        login_url,
        headers=headers,
        json=payload
    )
    assert response.status_code == 200
    return response.json()["AuthenticationResult"]["IdToken"]


@pytest.fixture(scope="session")
def session(token):
    session = requests.Session()
    session.headers.update({
        "Authorization": token,
        "Accept": "application/json"
    })
    return session