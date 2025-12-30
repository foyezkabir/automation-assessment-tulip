import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context arguments"""
    return {
        **browser_context_args,
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser to run in headed mode"""
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,  # Slow down operations by 500ms for better visibility
    }
