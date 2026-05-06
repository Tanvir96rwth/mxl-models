import pandas as pd

from mxlmodels import get_nguyen2026_tomato


def test_rhs() -> None:
    model = get_nguyen2026_tomato()
    expected = pd.Series(
        {
            "B0": 4.4411911744646204e-05,
            "B1": -1.6517560652573593e-09,
            "B2": -4.39952501380958e-05,
            "PQH2": -0.0003903518896777314,
            "ATP": -0.00044505190092536395,
            "H_lumen": -4.3580198572697035e-08,
            "delta_psi": -2.4528208304146345e-07,
            "Vx": -1.9312103081729493e-05,
            "PsbS": 5.5328539255942305e-06,
            "ATPactivity": 0.0,
            "K_lumen": 3.261128873962982e-17,
            "K_stroma": -3.261128873962982e-17,
        }
    )
    pd.testing.assert_series_equal(
        model.get_right_hand_side().loc[expected.index],
        expected,
        atol=1e-9,
        rtol=1e-9,
    )
