import os
from collections.abc import Generator
from typing import Any

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from onyx.db.engine.sql_engine import SqlEngine
from onyx.main import fetch_versioned_implementation
from onyx.utils.logger import setup_logger

logger = setup_logger()


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    # Set environment variables
    os.environ["ENABLE_PAID_ENTERPRISE_EDITION_FEATURES"] = "True"

    # Initialize TestClient with the FastAPI app
    app: FastAPI = fetch_versioned_implementation(
        module="onyx.main", attribute="get_application"
    )()
    client = TestClient(app)
    yield client


@pytest.fixture(scope="session", autouse=True)
def initialize_db() -> None:
    # Make sure that the db engine is initialized before any tests are run
    SqlEngine.init_engine(
        pool_size=10,
        max_overflow=5,
    )
