from typing import Any, Callable

class ConfigBuilder(object):
    
    config : dict = {}

    # Even if value evaluates to false the key gets added
    def strictAppendConfig(self, key : str, value: Any) -> None:
        self.config[key] = value

    # Only creates the key if the value is true (i.e. not null & len(value) > 0)
    def lenientAppendConfig(self, key : str, value : Any) -> None:
        if value:
            self.config[key] = value

    def evalAppendConfig(self, key : str, value : Any, f : Callable) -> None:
        if f(value):
            self.config[key] = value

    @classmethod
    def removeRedundancies(self, d : dict) -> dict:
        return { k : v for k, v in d.items() if v is not None }