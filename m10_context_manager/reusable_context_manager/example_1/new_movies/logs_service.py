class LogsService:
    def send_logs(self, logs: list[str]) -> None:
        for log in logs:
            print(log)
