from main import DateDiff
from datetime import datetime
import pytest


def test_days_difference():
    # Test positive difference
    date_diff = DateDiff("18/8/2008", "26/9/2008")
    assert date_diff.days_difference() == 39

    # Test negative difference
    date_diff = DateDiff("26/9/2008", "18/8/2008")
    assert date_diff.days_difference() == -39

    # Test zero difference
    date_diff = DateDiff("18/8/2008", "18/8/2008")
    assert date_diff.days_difference() == 0

    # Test invalid input
    with pytest.raises(ValueError):
        date_diff = DateDiff("18/8/2008", "31/9/2008")

