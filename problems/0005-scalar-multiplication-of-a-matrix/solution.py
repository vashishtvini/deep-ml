import numpy
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	matrix=numpy.array(matrix)
	return matrix*scalar