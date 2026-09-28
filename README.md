# Hotel Booking API Automation Framework

## Overview

This project is a Python-based API automation framework built with PyTest and Requests.

The framework automates functional and negative API testing for the Restful Booker Hotel Booking API. It covers authentication, booking creation, retrieval, update, deletion, and validation of negative scenarios.

The project is designed to demonstrate practical QA automation skills including API testing, PyTest fixtures, parametrization, assertions, authentication handling, and reusable API client methods.

## Tech Stack

* Python
* PyTest
* Requests
* REST API
* JSON
* Git / GitHub

## API Under Test

Restful Booker API

Base URL:

`https://restful-booker.herokuapp.com`

Main endpoints covered:

* `POST /auth` — Authentication
* `POST /booking` — Create booking
* `GET /booking/{id}` — Retrieve booking
* `PUT /booking/{id}` — Update booking
* `DELETE /booking/{id}` — Delete booking

## Project Structure

```text
api_automation_framework/
├── tests/
│   └── test_api.py
├── api/
│   ├── __init__.py
│   └── api_client.py
├── config.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Test Coverage

The framework covers:

### Authentication

* Valid credentials
* Invalid credentials
* Authentication token generation

### Booking Management

* Create booking
* Retrieve booking
* Update booking
* Delete booking

### Negative Testing

* Invalid booking IDs
* Invalid credentials
* Update without authentication
* Delete without authentication
* Invalid booking data

### PyTest Features

* Fixtures
* Parametrization
* Assertions
* Reusable API client
* Dynamic booking ID generation

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run all tests

```bash
pytest -v
```

### 3. Run tests with detailed output

```bash
pytest -v -s
```

## Test Results

All automated tests are currently passing successfully.

The framework validates both positive and negative API scenarios against the Restful Booker API.
