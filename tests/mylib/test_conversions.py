import pytest

from app.mylib.utils import convert_kelvin_to_celsius


@pytest.mark.parametrize("kelvin, celsius", [(273, 0), (0, -273), (300, 27)])
def test_k_to_c(kelvin, celsius):
    res_celsius = convert_kelvin_to_celsius(kelvin)

    assert celsius == res_celsius


