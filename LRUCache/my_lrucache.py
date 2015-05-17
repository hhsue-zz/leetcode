#!/usr/bin/python
import collections

# cache: oldest k -> k -> -k -> k -> newest k
# get removes k, and then sets k to newest k
# set moves k to newest k
class LRUCache: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        else: 
            return -1

my_cache = LRUCache(5)

my_cache.set('asdf','asdf')
my_cache.set('qwer','qwer')
my_cache.set('zxcv','zxcv')
my_cache.set('wert','wert')
my_cache.set('sdfg','sdfg')

print my_cache.cache

my_cache.get('asdf')

print my_cache.cache

my_cache.set('mmmm','mmmm')

print my_cache.cache


my_cache.get('vvvv')

print my_cache.cache


