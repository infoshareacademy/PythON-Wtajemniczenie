from datetime import datetime


def run_example():
    moment_in_time = datetime(2021, 2, 25, 10, 17, 25)
    print(moment_in_time, type(moment_in_time))
    moment_in_time_iso_string = moment_in_time.isoformat()
    print(moment_in_time_iso_string, type(moment_in_time_iso_string))
    # print(moment_in_time.isoformat(sep="*"))


if __name__ == "__main__":
    run_example()
