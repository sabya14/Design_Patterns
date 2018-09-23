"""
Abstract factory Revised.
This a a revised example for the abstract method for better understanding wrt to python
and has better real life approach.

Key point - Abstract creation of object depending on business logic , platform etc.
			So in this we in generally create an interface, in python use an callable for
			that create abstract factory objects.

			The abstract factory method is dependent on Concrete factory sub classes to actually return the
			product

			Advantages - Isolates concrete classes. Implementation is hidden from clients
						- We can switch across concrete factories easily.
			Disadvantage - Addition of new family is sometimes cumbersome. Not a big problem in python.
						- The product returned by abstract factory are of the abstract factory type, and the client
						does not know about the actual attributes of the base concrete class.
						( We may try to downcast but that may fail) .
						This a classic trade of a good and extensible interface.

			* Note : The  Concrete factory can use a factory method for each product creation.
			A concrete factory will return the actual product by overiding the
			abstract factory . Limitation is that very slightly different
			products we will need new factories. This can be solved by using prototype pattern.

			Now for the example -
			Classic scenario  - We have data sources of various type -
			Files - CSV, EXCEL
			Database - Oracle, MS SQL , so we will try address creation of data objects with this pattern
"""


class Data:
	"""
	Abstract Factory
	"""
	def __init__(self, source_type=None):
		# internal attribute which actually stores the concrete factory object
		self.source_type = source_type

	# Functions of the abstract factory
	def get_data_source(self):
		return "I am data of type:{}".format(self.source_type.data_type(self))


class FileData:
	""" A Concrete Product"""
	def data_type(self):
		return "File"

	def __str__(self):
		return "File"


class DataBaseData:
	""" A Concrete Product"""
	def data_type(self):
		return "Database"

	def __str__(self):
		return "Database"


if __name__ == "__main__":
	file_data = Data(FileData)
	database_data = Data(DataBaseData)
	print(file_data.get_data_source())
	print(database_data.get_data_source())
