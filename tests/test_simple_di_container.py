from simple_di_container import __version__, DIContainer
from pytest import raises


def test_version():
    assert __version__ == '0.1.0'

def test_container_resolves_registered_item():
    container = DIContainer()
    phrase = 'Beautiful sunshine'
    container.register('phrase', lambda: phrase)

    assert container.resolve('phrase') == phrase


def test_container_do_not_resolves_unregistered_item():
    container = DIContainer()
    phrase = 'Beautiful sunshine'
    container.register('phrase', lambda: phrase)

    with raises(ValueError):
        assert container.resolve('non-existing')
