from playwright.sync_api import APIRequestContext

class OicApi:

    def __init__(self, request: APIRequestContext):
        self.request = request

    def get_approved_coverageset(self, aggregation_id: str, medicaid_id: str):
        return self.request.get(f"/tpl-core/oic-api/{aggregation_id}/coverage/{medicaid_id}/approved"
    )

    def get_coverageset(self, aggregation_id: str, medicaid_id: str, coverage_set_id: str):
        return self.request.get(f"/tpl-core/oic-api/{aggregation_id}/coverage/{medicaid_id}"
            )
