# Python code​​​​​​‌‌​‌​​‌​‌​‌​‌​​‌‌‌‌‌‌​​‌​ below
class Shape:
	width = 5
	height = 5
	printChar = '#'

	def printRow(self, i):
		raise NotImplementedError("Will be implemented by children extending this class")

	def print(self):
		for i in range(self.height):
			self.printRow(i)


class Square(Shape):
	def printRow(self, i):
		print(self.printChar * self.width)

class Triangle(Shape):
	def printRow(self, i):
		# print(self.printChar * (i + 1))
		base = self.width * 2 - 1
		chars = i * 2 + 1
		spaces = (base - chars) // 2
		print(' ' * spaces + self.printChar * chars + ' ' * spaces)
		


t = Triangle()
t.print()