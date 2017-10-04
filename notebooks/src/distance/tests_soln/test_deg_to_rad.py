import great_circle
import numpy as np

def test_deg_to_rad():
    out = great_circle.deg_to_rad(180)
    assert np.allclose(out, np.pi)
