import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient=np.array(gradient,dtype=float)
	magnitude=np.linalg.norm(gradient)
	if magnitude==0:
		dire=np.zeros_like(gradient).tolist()
		descent_dire=np.zeros_like(gradient).tolist()
	else:
		dire=(gradient/magnitude).tolist()
		descent_dire=(-gradient/magnitude).tolist()
	return{
		'magnitude':magnitude,
		'direction':dire,
		'descent_direction':descent_dire
	}