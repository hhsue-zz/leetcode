#!/usr/bin/python
import collections

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

my_cache = LRUCache(10)

my_cache.set('asdf','asdf')
my_cache.set('qwer','qwer')
my_cache.set('zxcv','zxcv')
my_cache.set('wert','wert')
my_cache.set('sdfg','sdfg')

print my_cache.cache

my_cache.get('asdf')

print my_cache.cache
