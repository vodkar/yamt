
from tempfile import TemporaryDirectory

import pytest
from faker import Faker
from faker.providers import internet

from yamt.hosts import HostStorage


@pytest.fixture(scope="session")
def temp_dir():
    with TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture(scope="session")
def setup_faker_provider(faker: Faker):
    faker.add_provider(internet)



@pytest.fixture
def host_storage_path(temp_dir: str):
    return f"{temp_dir}/host_storage.yaml"


@pytest.fixture
def host_storage(host_storage_path: str) -> HostStorage:
    return HostStorage(host_storage_path)
