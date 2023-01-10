from imperial_to_metric import mph_to_kph


def transform_driver_race_laps(driver_race_laps: [{}]) -> [{}]:
    """
    This function receives a list of items. Each item represents a lap with the following information:
    - lap_number: int
    - average_speed: float.

    For example:
    {
        "lap_number": 1,
        "average_speed": 185.981
    }

    You must return a list with the same items but the speed must be transformed to the metric system. Since the speed given in the data from "driver_race_laps"
    uses the imperial system, you must import and use the function you have just implemented in imperial_to_metric.py

    :param driver_race_laps:
    :return:
    """
    # TODO 2:
    for race_lap in driver_race_laps:
        race_lap["average_speed"] = mph_to_kph(race_lap["average_speed"])
    return driver_race_laps


def get_lap_average_speed(lap_number: int, driver_race_laps: [{}]) -> float:
    # The python version used in GitHub does not like the real return type -> Any | None:
    """
    This function received a lap number and a list of items. Each item represents a lap with the following information:
    - lap_number: int
    - average_speed: float.

    For example:
    {
        "lap_number": 1,
        "average_speed": 185.981
    }

    You must find the lap that matches the lap_number searching inside the driver_race_laps and return the lap average speed.
    NOTE: If the lap_number is not found inside the driver_race_laps, then you should return None (this case dont worry about the return type should be a float)

    :param lap_number:
    :param driver_race_laps:
    :return:
    """
    # TODO 3:
    for lap_info in driver_race_laps:
        if lap_info["lap_number"] == lap_number:
            return lap_info["average_speed"]
    return None
