import pytest

from pymongo.mongo_client import MongoClient


class TestPymongoClient(object):

    def test_client(self, pymongo_client):
        assert type(pymongo_client) == MongoClient

    @pytest.mark.usefixtures('mock_pymongo_client')
    def test_drop_database(self, pymongo_client):
        database = pymongo_client.test_drop_database
        database.test_collection.insert_one({})

        names = pymongo_client.database_names()
        assert 'test_drop_database' in names

        pymongo_client.drop_database(database)

        names = pymongo_client.database_names()
        assert 'test_drop_database' not in names
