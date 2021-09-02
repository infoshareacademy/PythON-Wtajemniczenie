from example_system.config import Config


def run_example() -> None:
    user_arguments = {"DEBUG": "True"}
    env_file_config = {"ENV": "STAGING", "OPTIMIZED_MODE": "False", "LOGGING_LEVEL": "INFO"}
    defaults = {"DEBUG": "False", "ENV": "", "LOGS_DIR": "/var/log/", "LOGGING_LEVEL": "WARNING"}

    config = Config(user_arguments, env_file_config, defaults)

    print(config.get_key("DEBUG"))
    print(config.get_key("ENV"))
    print(config.get_key("OPTIMIZED_MODE"))
    print(config.get_key("LOGGING_LEVEL"))
    print(config.get_key("LOGS_DIR"))


if __name__ == "__main__":
    run_example()
