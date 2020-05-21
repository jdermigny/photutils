# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This module provides tools for generating matplotlib colormaps.
"""

import numpy as np

from .check_random_state import check_random_state

__all__ = ['make_random_cmap']


def make_random_cmap(ncolors=256, random_state=None):
    """
    Make a matplotlib colormap consisting of (random) muted colors.

    A random colormap is very useful for plotting segmentation images.

    Parameters
    ----------
    ncolors : int, optional
        The number of colors in the colormap.  The default is 256.

    random_state : int or `~numpy.random.RandomState`, optional
        The pseudo-random number generator state used for random
        sampling.  Separate function calls with the same
        ``random_state`` will generate the same colormap.

    Returns
    -------
    cmap : `matplotlib.colors.ListedColormap`
        The matplotlib colormap with random colors.
    """

    from matplotlib import colors

    prng = check_random_state(random_state)
    hue = prng.uniform(low=0.0, high=1.0, size=ncolors)
    sat = prng.uniform(low=0.2, high=0.7, size=ncolors)
    val = prng.uniform(low=0.5, high=1.0, size=ncolors)
    hsv = np.dstack((hue, sat, val))
    rgb = np.squeeze(colors.hsv_to_rgb(hsv))

    return colors.ListedColormap(rgb)
