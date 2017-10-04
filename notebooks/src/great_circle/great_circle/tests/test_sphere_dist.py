import numpy as np
import great_circle

london = (51.5, -0.1)
nyc = (40.7, -74.0)

correct = 5879.7014885816379

def test_sphere_dist():
    out = great_circle.sphere_dist(london,nyc)

    assert np.allclose(out,correct)

