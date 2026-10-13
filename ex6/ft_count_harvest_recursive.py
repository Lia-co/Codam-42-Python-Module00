def ft_count_harvest_recursive() -> None:
    harvest_day = int(input("Days until harvest: "))

    def count_days(current_day: int) -> None:
        if current_day > harvest_day:
            return
        else:
            print(f"Day {current_day}")
            count_days(current_day + 1)
    count_days(1)
    print("Harvest time!")
