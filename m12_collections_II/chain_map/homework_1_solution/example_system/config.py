from collections import ChainMap


class Config:
    def __init__(
        self, arguments: dict[str, str], config_file: dict[str, str], defaults: dict[str, str]
    ) -> None:
        self.arguments = arguments
        self.config_file = config_file
        self.defaults = defaults
        self.overall_config = ChainMap(arguments, config_file, defaults)

    def get_key(self, config_key_name: str) -> str:
        return self.overall_config[config_key_name]
