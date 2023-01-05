from math import inf

import pytest

from imperial_to_metric import mph_to_kph

testdata_imperial_to_metric = [
    (0, 0),
    (1, 1.60934),
    (100, 160.934),
    (200, 321.868),
    (-1, -1.60934),
    (inf, inf),
    (-inf, -inf)
]


@pytest.mark.parametrize("mph, expected_pkh", testdata_imperial_to_metric)
def test_imperial_to_metric(mph, expected_pkh):
    assert expected_pkh == pytest.approx(mph_to_kph(mph), 0.01)
