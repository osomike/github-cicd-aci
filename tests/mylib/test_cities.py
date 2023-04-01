import pytest

from app.mylib.cities import get_lat_long


@pytest.mark.parametrize("city, country, lat, long", [
    ('Amsterdam', 'Netherlands', 52.3667, 4.8833),
    ('Paris', 'France', 48.8566, 2.3522),
    ('Berlin', 'Germany', 52.5167, 13.3833)])
def test_get_lat_long(city, country, lat, long):

    res_lat, res_long = get_lat_long(country, city)

    assert lat == res_lat
    assert long == res_long
