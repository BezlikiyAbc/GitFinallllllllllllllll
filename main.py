import math

class Shape:
	def __init__(self):
		self._Position=0
		self._Scale=0
		self._Color=0

	def get_position(self):
		return self._Position
	def set_position(self, pos):
		self._Position = pos

	def get_scale(self):
		return self._Scale
	def set_scale(self, scale):
		self._Scale = scale

	def get_Color(self):
		return self._Color
	def set_Color(self, color):
		self._Color = color

	def info(self):
		print('Position - ', self._Position, '\nScale - ', self._Scale, '\nColor - ', self._Color)

	def area(self):
		print('Площядь фигуры:')

class Rectangle(Shape):
	def __init__(self):
		Shape.__init__(self)
		self._Side1 = 0
		self._Side2 = 0

	def get_Side1(self):
		return self._Side1
	def set_Side1(self, side):
		self._Side1 = side

	def get_Side2(self):
		return self._Side2
	def set_Side2(self, side):
		self._Side2 = side

	def info(self):
		super().info()
		print('Side1 - ', self._Side1, '\nSide1 - ', self._Side1)

	def area(self):
		super().area()
		print(self._Side1 * self._Side2)

class Trapezod(Shape):
	def __init__(self):
		Shape.__init__(self)
		self._Side1 = 0
		self._Side2 = 0
		self._H = 0

	def get_Side1(self):
		return self._Side1
	def set_Side1(self, side):
		self._Side1 = side

	def get_Side2(self):
		return self._Side2
	def set_Side2(self, side):
		self._Side2 = side

	def get_H(self):
		return self._H
	def set_H(self, h):
		self._H = h

	def info(self):
		super().info()
		print('Side1 - ', self._Side1, '\nSide1 - ', self._Side1, '\nH - ', self._H)

	def area(self):
		super().area()
		print(0.5 * (self._Side1 + self._Side2) * self._H)

class Circle(Shape):
	def __init__(self):
		Shape.__init__(self)
		self._Radius = 0

	def get_Radius(self):
		return self._Radius
	def set_Radius(self, radius):
		self._Radius = radius

	def info(self):
		super().info()
		print('Radius - ', self._Radius)

	def area(self):
		super().area()
		print(math.pi * (self._Radius * self._Radius))

rect = Rectangle()
rect.set_Side1(10)
rect.set_Side2(5)
rect.set_position([10, 10])
rect.set_scale(1)
rect.set_Color('r-255, g-0, b-0')
rect.info()
rect.area()

trapezoid = Trapezoid()
trapezoid.set_Side1(10)
trapezoid.set_Side2(5)
trapezoid.set_position([-10, 10])
trapezoid.set_scale(1)
trapezoid.set_Color('r-0, g-255, b-0')
trapezoid.set_H(10)
trapezoid.info()
trapezoid.area()

circle = Circle()
circle.set_Radius(10)
circle.set_position([10, -10])
circle.set_scale(1)
circle.set_Color('r-0, g-0, b-255')
circle.info()
circle.area()