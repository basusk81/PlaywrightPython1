import pytest
from clients.oic_api import OicApi/

@pytest.fixture
def oic_api(api_context):
    return OicApi(api_context)

def test_get_approved_coverageset(oic_api):
    aggregation_id = "michigan"
    medicaid_id = "67890"

    response = oic_api.get_approved_coverageset(aggregation_id, medicaid_id)

    assert response.ok
    assert response.status == 200

    if response.status == 200:
        body = response.json()
        assert body["id"] == medicaid_id

@pytest.mark.parametrize(
    "aggregation_id, medicaid_id, expected_status",
    [
        ("michigan", "67890", 200)
     ]
)
def test_get_approved_coverageset(oic_api, aggregation_id, medicaid_id, expected_status):
    response = oic_api.get_approved_coverageset(aggregation_id, medicaid_id)

    assert response.status == expected_status

    if response.status == 200:
        body = response.json()
        assert body["id"] == medicaid_id