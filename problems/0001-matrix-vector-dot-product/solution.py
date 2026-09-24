import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not b:
		return -1
	col=len(a[0])
	vector_len=len(b)

	if col!= vector_len:
		return -1
	res=np.dot(a,b)
	return res.tolist()