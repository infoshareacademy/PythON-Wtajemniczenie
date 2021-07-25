from __future__ import annotations


class PhoneApps:
    def __init__(self) -> None:
        self.system_apps: list[str] = []
        self.user_apps: list[str] = []

    def install_system_apps(self, app: str) -> None:
        self.system_apps.append(app)

    def install_user_apps(self, app: str) -> None:
        self.user_apps.append(app)

    def __iter__(self) -> AppsIterator:
        return AppsIterator(self.system_apps, self.user_apps)


class AppsIterator:
    def __init__(self, system_apps: list[str], user_apps: list[str]) -> None:
        self.system_apps = system_apps
        self.user_apps = user_apps
        self.system_apps_index = 0
        self.user_apps_index = 0

    def __iter__(self) -> AppsIterator:
        return self

    def __next__(self) -> str:
        while self.system_apps_index < len(self.system_apps):
            element_to_return = self.system_apps[self.system_apps_index]
            self.system_apps_index += 1
            return element_to_return

        while self.user_apps_index < len(self.user_apps):
            element_to_return = self.user_apps[self.user_apps_index]
            self.user_apps_index += 1
            return element_to_return

        raise StopIteration()


def run_example() -> None:
    my_apps = PhoneApps()
    my_apps.install_system_apps("App Store")
    my_apps.install_user_apps("Strava")
    my_apps.install_user_apps("Spotify")

    for app in my_apps:
        print(app)


if __name__ == "__main__":
    run_example()
