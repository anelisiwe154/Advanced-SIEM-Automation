import pytest
from code_implem.factories.repository_factory import RepositoryFactory
from code_implem.repositories.inmemory.inmemory_alert_repository import InMemoryAlertRepository
from code_implem.repositories.inmemory.inmemory_incident_repository import InMemoryIncidentRepository
from code_implem.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from code_implem.repositories.inmemory.inmemory_rule_repository import InMemoryRuleRepository
from code_implem.repositories.database.database_alert_repository import DatabaseAlertRepository
from code_implem.repositories.filesystem.filesystem_alert_repository import FileSystemAlertRepository
from code_implem.src.alert import Alert


def test_factory_returns_alert_repo():
    repo = RepositoryFactory.get_repository("ALERT", "MEMORY")
    assert isinstance(repo, InMemoryAlertRepository)


def test_factory_returns_incident_repo():
    repo = RepositoryFactory.get_repository("INCIDENT", "MEMORY")
    assert isinstance(repo, InMemoryIncidentRepository)


def test_factory_returns_user_repo():
    repo = RepositoryFactory.get_repository("USER", "MEMORY")
    assert isinstance(repo, InMemoryUserRepository)


def test_factory_returns_rule_repo():
    repo = RepositoryFactory.get_repository("RULE", "MEMORY")
    assert isinstance(repo, InMemoryRuleRepository)


def test_factory_invalid_entity():
    with pytest.raises(ValueError):
        RepositoryFactory.get_repository("UNKNOWN", "MEMORY")


def test_factory_invalid_storage():
    with pytest.raises(ValueError):
        RepositoryFactory.get_repository("ALERT", "INVALID")


def test_factory_database_stub_methods_raise():
    repo = RepositoryFactory.get_repository("ALERT", "DATABASE")
    assert isinstance(repo, DatabaseAlertRepository)
    dummy_alert = Alert("1","Test Alert","Rule1","Event","High","2026-05-09","2026-05-09",
                        "Category","SubCategory","Tactic","Tag","127.0.0.1",1)
    with pytest.raises(NotImplementedError):
        repo.save(dummy_alert)


def test_factory_filesystem_stub_methods_raise():
    repo = RepositoryFactory.get_repository("ALERT", "FILESYSTEM")
    assert isinstance(repo, FileSystemAlertRepository)
    dummy_alert = Alert("1","Test Alert","Rule1","Event","High","2026-05-09","2026-05-09",
                        "Category","SubCategory","Tactic","Tag","127.0.0.1",1)
    with pytest.raises(NotImplementedError):
        repo.save(dummy_alert)

