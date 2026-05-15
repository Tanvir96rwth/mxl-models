import pandas as pd

from mxlmodels import get_dynamic_enterobactin


def test_rhs() -> None:
    model = get_dynamic_enterobactin()
    expected = pd.Series(
        {
            "x1": 0.12093348356070453,
            "x2": 0.2355964874705504,
            "s1": -0.7399340495204443,
            "p1": 0.0002614990261410044,
        }
    )
    pd.testing.assert_series_equal(
        model.get_right_hand_side().loc[expected.index],
        expected,
        atol=1e-9,
        rtol=1e-9,
    )
