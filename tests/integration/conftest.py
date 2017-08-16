import mock
import pytest

from mongomock.mongo_client import MongoClient

from kore import config_factory, container_factory


@pytest.fixture(scope='session')
def pymongo_config():
    return {
        'url': 'mongodb://user:pass@localhost',
    }


@pytest.fixture(scope='session')
def config(pymongo_config):
    return config_factory.create('dict', **{'pymongo': pymongo_config})


@pytest.fixture
def container(config):
    initial = {
        'config': config,
    }
    return container_factory.create(**initial)


@pytest.fixture
def pymongo_client(container):
    return container('kore.components.pymongo.client')


@pytest.yield_fixture
def mock_pymongo_client():
    with mock.patch(
        'kore_plugins_pymongo.plugins.pymongo.MongoClient',
        new=MongoClient,
    ) as m:
        yield m
