from math import inf

import pytest

from data_analysis import get_lap_average_speed
from imperial_to_metric import mph_to_kph

testdata_get_lap = [
    (
        [
            {
                "lap_number": 5,
                "average_speed": 299.306
            },
            {
                "lap_number": 2,
                "average_speed": 298.184
            },
            {
                "lap_number": 4,
                "average_speed": 299.338
            },
            {
                "lap_number": 1,
                "average_speed": 299.535
            },
            {
                "lap_number": 3,
                "average_speed": 296.438
            },
        ], 0, None
    ),
    (
        [
            {
                "lap_number": 5,
                "average_speed": 299.306
            },
            {
                "lap_number": 2,
                "average_speed": 298.184
            },
            {
                "lap_number": 4,
                "average_speed": 299.338
            },
            {
                "lap_number": 1,
                "average_speed": 299.535
            },
            {
                "lap_number": 3,
                "average_speed": 296.438
            },
        ], 1, 299.535
    ),
    (
        [], 10, None
    ),
    (
        [
            {
                "lap_number": 5,
                "average_speed": 299.306
            },
            {
                "lap_number": 2,
                "average_speed": 298.184
            },
            {
                "lap_number": 4,
                "average_speed": 299.338
            },
            {
                "lap_number": 1,
                "average_speed": 299.535
            },
            {
                "lap_number": 3,
                "average_speed": 296.438
            },
        ], 5, 299.306
    ),
]


@pytest.mark.parametrize("driver_race_laps, lap_number, expected_average_speed", testdata_get_lap)
def test_imperial_to_metric(driver_race_laps, lap_number, expected_average_speed):
    assert get_lap_average_speed(driver_race_laps=driver_race_laps, lap_number=lap_number) == expected_average_speed
