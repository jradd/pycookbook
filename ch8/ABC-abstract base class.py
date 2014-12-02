'Defining an Interface or Abstract Base Class'

from abs import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
	@abstractmethod
	def read(self, maxbytes= -1):
		pass
	@abstractmethod
	def write(self, data):
		pass


a = IStream()