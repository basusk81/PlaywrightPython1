import yaml
import pytest

@pytest.fixture(scope="session")
def test_data():
    with open("data/userdata.yaml", "r") as file:
        data = yaml.safe_load(file)
    return data["test_env"]
