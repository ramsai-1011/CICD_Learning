import pytest

from mlops_project.variable_flow import validate_pair


def test_valid_pair_sums_to_100() -> None:
    assert validate_pair(40, 60) == (40, 60)


def test_invalid_pair_raises_error() -> None:
    with pytest.raises(ValueError, match="must sum to 100"):
        validate_pair(30, 50)
