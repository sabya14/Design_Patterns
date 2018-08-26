"""
	Abstract Factory
	Simple implementation of abstract factory pattern.
	Provide interface for creating families of related or dependent objects without
	specifying the concrete classes

	System is independent of how a product is created, composed or represented.
"""

# Import abstract base classes package
import abc


class Car(abc.ABC):
	"""
	The main abstract class. Only contains interfaces not implementation
	Interfaces for operations that create a car
	"""
	@abc.abstractmethod
	def create_body(self):
		pass

	@abc.abstractmethod
	def create_engine(self):
		pass


class SuperCar(Car):
	"""
	Concrete class super car for abstract class Car.
	Contain implementations of all the abstract methods
	"""
	def create_body(self):
		return SuperCarBody()

	def create_engine(self):
		return SuperCarEngine()


class NormalCar(Car):
	"""
	Concrete class normal car for abstract class Car.
	Contain implementations of all the abstract methods

	"""
	def create_body(self):
		return NormalCarBody()

	def create_engine(self):
		return NormalCarEngine()


class Engine(abc.ABC):
	"""
	Instead of directly defining or returning a engine type, we create a abstract class for it also. Because all the
	engine type objects for a car will be highly related
	"""
	@abc.abstractmethod
	def engine_power(self):
		pass


class Body(abc.ABC):
	"""
	Instead of directly defining or returning a body type, we create a abstract class for it also. Because all the
	body type objects for a car will be highly related
	"""
	@abc.abstractmethod
	def body_shape(self):
		pass


class SuperCarEngine(Engine):
	"""
	Concrete class for the super car engine
	"""
	def engine_power(self):
		print("Super Car Engine will be returned")


class NormalCarEngine(Engine):
	"""
	Concrete class for the normal car engine
	"""

	def engine_power(self):
		print("Normal Car Engine will be returned")


class SuperCarBody(Body):
	"""
	Concrete class for the super car body
	"""

	def body_shape(self):
		print("Racing type body")


class NormalCarBody(Body):
	"""
	Concrete class for the normal car body
	"""
	def body_shape(self):
		print("Normal sedan type body")


if __name__ == '__main__':
	for factory in (SuperCar(), NormalCar()):
		engine = factory.create_engine()
		body = factory.create_body()
		engine.engine_power()
		body.body_shape()
