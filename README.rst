# simple_di_container
`simple_di_container` is dependency injection container library for Python inspired by dry-container.

## Installation
```
pip install simple_di_container
```
or with poetry
```
poetry add simple_di_container
```

## Examples
Stabbing dependencies with side-effects
```python
from simple_di_container import DIContainer

class AppContainer(DIContainer):

    def initialize(self) -> None:
        if os.getenv('ENV') == 'test':
            self.register('github_api_service', lambda: GithibApiServiceStub)
        else:
            self.register('github_api_service', lambda: GithibApiService)


container = AppContainer()

service = container.resolve('github_api_service')()
```

