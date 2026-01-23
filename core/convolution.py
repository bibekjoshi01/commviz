import numpy as np


def stepwise_convolution(x, h):
    """
    Compute stepwise convolution arrays for animation.
    Returns a list of outputs for each shift.
    """
    n_x = len(x)
    n_h = len(h)
    n_out = n_x + n_h - 1

    y_full = np.convolve(x, h, mode="full")
    outputs = []

    # Step through each time shift of h
    for i in range(n_out):
        # Zero-pad h to match full length and shift
        h_shifted = np.zeros(n_out)
        if i < n_h:
            h_shifted[i : i + n_h] = h[: n_h - i]
        else:
            h_shifted[i : i + n_h] = h
        outputs.append(y_full[:n_out])
    return outputs, y_full
