import pandas as pd

from mxlmodels import get_nguyen2026_tomato


def test_rhs() -> None:
    model = get_nguyen2026_tomato()
    expected = pd.Series(
        {
            "B0": -50.0,
            "B1": 50.0,
            "B2": 0.0,
            "PQH2": 4.211175506040631e-13,
            "ATP": -257.64738716262366,
            "H_lumen": 0.35687759512106204,
            "delta_psi": 2.008611194639914,
            "Vx": -9.599999040000053e-11,
            "PsbS": -4.663742428143797e-06,
            "ATPactivity": 0.009000000000000001,
            "K_lumen": 1.437486414617514e-23,
            "K_stroma": -1.437486414617514e-23,
        }
    )
    pd.testing.assert_series_equal(
        model.get_right_hand_side().loc[expected.index],
        expected,
        atol=1e-9,
        rtol=1e-9,
    )
