#!/usr/bin/env python3
'''A module for using the Redis NoSQL data storage.
'''

from typing import Union
import redis
import uuid


class Cache:
    '''Represents an object for storing data in a Redis data storage.
    '''

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data:  Union[str, bytes, int, float]) -> str:
        '''Stores a value in a Redis data storage and returns the key.
        '''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
