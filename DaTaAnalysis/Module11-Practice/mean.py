'''https://www.deep-ml.com/problems/4'''

import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    a = np.array(matrix)

    if mode == 'column':
        return np.mean(a, axis=0)
    else:
        return np.mean(a, axis=1)
