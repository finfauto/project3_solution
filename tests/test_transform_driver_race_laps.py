from math import inf

import pytest

from data_analysis import transform_driver_race_laps
from imperial_to_metric import mph_to_kph

testdata_transform_driver_race_laps = [
    (
        [
            {
                "lap_number": 5,
                "average_speed": 185.981
            },
            {
                "lap_number": 2,
                "average_speed": 185.284
            },
            {
                "lap_number": 4,
                "average_speed": 186.001
            },
            {
                "lap_number": 1,
                "average_speed": 186.123
            },
            {
                "lap_number": 3,
                "average_speed": 184.199
            },
        ],
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
        ],
    ),
    (
        [
        ],
        [
        ],
    ),
    (
        [
            {
                "lap_number": 5,
                "average_speed": 185.981
            },
            {
                "lap_number": 5,
                "average_speed": 185.981
            },
        ],
        [
            {
                "lap_number": 5,
                "average_speed": 299.306
            },
            {
                "lap_number": 5,
                "average_speed": 299.306
            },
        ],
    ),
]


@pytest.mark.parametrize("race_laps, expected_race_laps", testdata_transform_driver_race_laps)
def test_imperial_to_metric(race_laps, expected_race_laps):
    transformed_race_laps = transform_driver_race_laps(race_laps)
    assert len(transformed_race_laps) == len(expected_race_laps)
    for expected_race_lap in expected_race_laps:
        for transformed_race_lap in transformed_race_laps:
            if expected_race_lap["lap_number"] == transformed_race_lap["lap_number"]:
                assert expected_race_lap["average_speed"] == pytest.approx(transformed_race_lap["average_speed"], 0.01)
                transformed_race_laps.remove(transformed_race_lap)
    assert len(transformed_race_laps) == 0
