#_*_ coding:utf-8 _*_

from django.core.cache import get_cache
from django_redis import get_redis_connection


class DefualtRedisPool(ConnectionFactory):
    def get_connection_pool(self, params={}):

        r = get_redis_connection(
            "default"
        )  # Use the name you have defined for Redis in settings.CACHES
        connection_pool = r.connection_pool
        print("Created connections so far: %d" %
              connection_pool._created_connections)

    def get_connection(self, params={}):

        pass

    def get_or_create_connection_pool(self, params: dict):
        # This is a high layer on top of `get_connection_pool` for
        # implementing a cache of created connection pools.
        # It should be overwritten if you want change the default
        # behavior.
        pass

    def make_connection_params(self, url: str) -> dict:
        # The responsibility of this method is to convert basic connection
        # parameters and other settings to fully connection pool ready
        # connection parameters.
        pass

    def connect(self, url: str):
        # This is really a public API and entry point for this
        # factory class. This encapsulates the main logic of creating
        # the previously mentioned `params` using `make_connection_params`
        # and creating a new connection using the `get_connection` method.
        pass
