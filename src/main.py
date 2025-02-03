from random import choices
from manim import (
	Scene, 
	Dot, 
	VGroup, 
	GREEN
)

# reduce this if it takes too long to render, reduce the scale so it is not as noticable
NUMBER_OF_POINTS = 20000
# reduce if you are increasing the number of points or scale because it can get messy
DOT_RADIUS = 0.01 

def fern(scale: float, x_shift: float, y_shift: float):
	"""fern generation algorithm which generates all the location of dots that make up the fern,
		use `f = fern()` to create a generator and `next(f)` to get the next coordinates

	Args:
		scale (float): allows the image to be scaled to be made bigger or smaller
		y_shift (float): moves the image in the y-direction, useful for making it fit on screen
		x_shift (float): moves the image in the x-direction, usually not needed

	Yields:
		_type_: coordinates of the next dot
	"""
	x, y = 0, 0

	options = [0, 1, 2, 3]
	weights = [0.01, 0.85, 0.07, 0.07] # probabilities can be adjusted here which makes the fern look different

	while True:
		c = choices(options, weights)[0]

		if c == 0:
			x, y = 0, 0.16 * y
		elif c == 1:
			x, y = (0.85 * x) + (0.04 * y), (-0.04 * x) + (0.85 * y) + 1.6
		elif c == 2:
			x, y = (0.2 * x) - (0.26 * y), (0.23 * x) + (0.22 * y) + 1.6
		elif c == 3:
			x, y = (-0.15 * x) + (0.28 * y), (0.26 * x) + (0.24 * y) + 0.44

		yield ((x * scale) + x_shift, (y * scale) + y_shift)


class BarnsleyFern(Scene):
	def construct(self):
		# if you reduce the number of points reduce the scale as well so it is not as noticable
		fern_point = fern(scale=0.75, x_shift=0, y_shift=-3.8)
		points = VGroup()

		for _ in range(NUMBER_OF_POINTS):
			x, y = next(fern_point)
			points.add(Dot([x, y, 0], radius=0.01, color=GREEN))

		self.add(points)