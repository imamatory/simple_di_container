from contextlib import contextmanager
from functools import cache
from types import LambdaType
from typing import Any


class DIItem:
    _item: Any
    _options: dict

    _default_options = {
        'call': True
    }

    def __init__(self, item: Any, options: dict) -> None:
        self._item = item
        self._options = {**self._default_options, **options}

    def get_value(self):
        return self._item() if self._options.get('call') and isinstance(self._item, LambdaType) else self._item


class DIContainer:
    _container: dict[str, DIItem] = {}

    def initialize(self):
        raise NotImplementedError

    @cache
    def _initialize(self):
        """Use @cache decorator to initialize container once."""
        self.initialize()

    def register(self, key, obj, **kwargs):
        if key in self._container:
            raise ValueError(f'There is already an item registered with the key {key}')
        self._register_item(key, DIItem(obj, kwargs))

    @contextmanager
    def override(self, key, new_obj, **kwargs):
        self._initialize()
        existing_item = self._resolve_item(key)
        self._register_item(key, DIItem(new_obj, kwargs))
        yield
        self._register_item(key, existing_item)

    def resolve(self, key):
        self._initialize()
        return self._resolve_item(key).get_value()

    def _resolve_item(self, key):
        if key not in self._container:
            raise AttributeError(f'Nothing registered with the key "{key}"')
        return self._container[key]

    def _register_item(self, key: str, item: DIItem):
        self._container[key] = item
