# ProGlove Automation Tests

## Overview
This repository contains automated API tests developed as part of the ProGlove automation task.
The project focuses on validating API functionality, request/response handling, and integration between hardware-related workflows and software services.

## Tech Stack
- Python
- Pytest
- Requests

## Project Structure
```
proglove-automation/
├── tests/              # Automated test cases
├── requirements.txt    # Project dependencies
├── .env                # Environment configuration
└── README.md
```

## Setup
Clone the repository:

```
git clone <repository-url>
```

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Configuration
Configure the required environment variables in a `.env` file.
Do not commit credentials or sensitive configuration.

## Run Tests

Run the complete test suite:
```
pytest
```

Run tests with verbose output:
```
pytest -v -s
```