# import pytest

# from playwright.sync_api import APIRequestContext, Playwright
# from config.config import Config

# @pytest.fixture(scope="session")
# def api_context(playwright: Playwright) -> APIRequestContext:

#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#     }

#     if Config.API_TOKEN:
#         headers["x-api-key"] = f"Bearer{Config.API_TOKEN}"

#     context = playwright.request.new_context(
#         base_url=Config.OIC_API_BASE_URL,
#         extra_http_headers=headers,
#         timeout=30000
#   )

#     yield context

#     context.dispose()
#   # Set a timeout of 60 seconds
