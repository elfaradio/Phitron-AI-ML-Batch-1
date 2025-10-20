import numpy as np

# Example matrix
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Compute the SVD
U, S, Vt = np.linalg.svd(A)
print(U, S, Vt)
# Rank of A
rank = np.linalg.matrix_rank(A)

# Columns of U corresponding to non-zero singular values form a basis of the column space
image_basis = U[:, :rank]

print("Basis of the image (column space):")
print(image_basis)
