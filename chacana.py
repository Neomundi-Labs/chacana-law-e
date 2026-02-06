import numpy as np

def chacana_points(
    scale=1.0,
    center=(0.0, 0.0)
):
    """
    Generates the minimal point structure of a Chakana (Andean cross).

    The Chakana is represented as an orthogonal stepped cross
    with a central void. This function encodes no dynamics,
    control, or optimization logic.

    Parameters
    ----------
    scale : float
        Global scaling factor.
    center : tuple
        (x, y) coordinates of the center.

    Returns
    -------
    points : np.ndarray
        Array of 2D points defining the Chakana structure.
    """

    cx, cy = center

    base = np.array([
        (-1, -3), (1, -3),
        (-1, -1), (1, -1),
        (-3, -1), (-3, 1),
        (-1, 1), (1, 1),
        (3, 1), (3, -1),
        (1, -1), (1, 1),
        (1, 3), (-1, 3),
        (-1, 1), (-1, -1)
    ], dtype=float)

    points = scale * base + np.array([cx, cy])
    return points
