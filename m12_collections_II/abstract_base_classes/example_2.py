from collections.abc import Sequence


class PhoneApps(Sequence):
    def __init__(self) -> None:
        self.system_apps: list[str] = []
        self.user_apps: list[str] = []

    def install_system_apps(self, app: str) -> None:
        self.system_apps.append(app)

    def install_user_apps(self, app: str) -> None:
        self.user_apps.append(app)

    def __getitem__(self, index: int) -> str:
        if index < len(self.system_apps):
            return self.system_apps[index]

        index -= len(self.system_apps)
        return self.user_apps[index]

    def __len__(self) -> int:
        return len(self.system_apps) + len(self.user_apps)


def run_example() -> None:
    my_apps = PhoneApps()
    my_apps.install_system_apps("App Store")
    my_apps.install_user_apps("Strava")
    my_apps.install_user_apps("Spotify")

    print(my_apps[0])
    print(my_apps[1])
    print(my_apps[2])

    print(len(my_apps))

    print(my_apps.index("Strava"))


if __name__ == "__main__":
    run_example()
