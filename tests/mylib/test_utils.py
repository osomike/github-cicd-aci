import pytest

from app.mylib.utils import convert_kelvin_to_celsius, add_additional_info


@pytest.mark.parametrize("kelvin, celsius", [(273, 0), (0, -273), (300, 27)])
def test_k_to_c(kelvin, celsius):
    res_celsius = convert_kelvin_to_celsius(kelvin)

    assert celsius == res_celsius


@pytest.mark.parametrize("dict_a, dict_b, dict_c", [
    ({1: 2}, {2: 3}, {1: 2, 2: 3}),
    ({1: 2}, {}, {1: 2}),
    ({}, {1: 2}, {1: 2})])
def test_add_additional_info(dict_a, dict_b, dict_c):
    res_dict = add_additional_info(dict_a, dict_b)

    assert dict_c == res_dict
