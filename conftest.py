
import pytest
from seleniumbase import BaseCase

@pytest.fixture(autouse=True)
def setup_teardown(request):
    """
    Global setup and teardown for all tests.
    Useful for initializing execution context, logging, or handling failures.
    """
    # Setup
    yield
    # Teardown
    if request.node.rep_call.failed:
        # Example: Take extra screenshot or log specific error on failure
        pass

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to access test result status in fixtures.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
