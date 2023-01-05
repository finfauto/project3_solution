def mph_to_kph(speed_in_mph: float) -> float:
    """
    Helper function to translate an input in miles per hour to kilometers per hour

    1 mile -> 1.60934 kilometers
    100 miles -> 160.934 kilometers
    200 miles -> 321.868 kilometers

    :param speed_in_mph: float
    :return: float
    """
    # TODO 1:
    # Write the formula that makes the conversion from miles per hour to kilometers per hour
    return speed_in_mph * 1.60934
