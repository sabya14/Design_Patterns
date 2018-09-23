"""
Abstract factory Revised.
This a a revised example for the abstract method for better understanding wrt to python
and has better real life approach.

Key point - Abstract creation of object depending on business logic , platform etc.
			Please refer to the abstract_factory_simple before reading this.

			In the last class we used simple concrete factory classes to build the actual products.
			But in general we use the factory method or the prototype method for it.
			Here we will make use of factory method
"""


class Data:
	"""
		Abstract Factory of Data
	"""
	def __init__(self, source_type=None):
		"""
			:param source_type:
			Any kind of factory implementation can be provided, provided the have the function necessary
			for the abstract factory, or the have overriden all the neccesary function of the abstract factory
		"""

		self.source_type = source_type

	def get_data_type(self):
		return "I am data of type:{}".format(self.source_type.data_type())


class FileData:
	"""
	This is a factory interface. It know how to create different kind of File Data.
	Any method of abstract factory have to implement here.

	File Data which is actually an interface to create Concrete Files(Concrete Products)
	Now this class will have a factory method which will specify which subclass object to create
	We make the factory method a static method
	Static method do not have access to data of the object.
	"""
	# This is the factory method which call the respective Concrete Product subclasses
	@staticmethod
	def factory(data_type):
		if data_type == 'csv':
			return CSVFileData()
		else:
			return ExcelFileData()

	def __str__(self):
		return "File"


class CSVFileData(FileData):
	def data_type(self):
		return "File: CSV"


class ExcelFileData(FileData):
	def data_type(self):
		return "File: CSV"


class DataBaseData:
	""" Data Data which is actually an interface to create Concrete DatabaseData(Concrete Products)"""
	@staticmethod
	def factory(data_type):
		if data_type == 'oracle':
			return OracleDataBase()
		else:
			return MSSQLDataBase()

	def __str__(self):
		return "Database"


class OracleDataBase(DataBaseData):

	def data_type(self):
		return "Database: Oracle"


class MSSQLDataBase(DataBaseData):

	def data_type(self):
		return "Database: MSSQL"


if __name__ == "__main__":
	""" 
	We create csv type data without actually knowing what is the base class.
	"""
	# we pass on a string parameter to help identify which type of object to create
	csv_file_data = Data(FileData.factory('csv'))
	oracle_database_data = Data(DataBaseData.factory('oracle'))

	print(csv_file_data.get_data_type())
	print(oracle_database_data.get_data_type())
	print("the disadvantage the dont know the actual base class")
	print(type(csv_file_data), type(oracle_database_data))