import pytest
from code_implem.src.user import User

def test_user_login_sets_state():
    user = User("u123", "pass123", "Afrocentric IP", "en-ZA")
    result = user.login()
    assert result == "User u123 logged in."
    assert user.is_logged_in is True

def test_user_logout_resets_state():
    user = User("u123", "pass123", "Afrocentric IP", "en-ZA")
    user.login()
    result = user.logout()
    assert result == "User u123 logged out."
    assert user.is_logged_in is False


def test_user_view_dashboard_requires_login():
    user = User("u123", "pass123", "Afrocentric IP", "en-ZA")
    # Not logged in yet
    with pytest.raises(PermissionError):
        user.view_dashboard()

    
    user.login()
    dashboard = user.view_dashboard()
    assert "Dashboard" in dashboard
    assert user.organisation in dashboard

