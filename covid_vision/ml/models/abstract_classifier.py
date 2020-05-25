import abc


class ClassifierInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_model') and
                callable(subclass.load_model) and
                hasattr(subclass, 'predict') and
                callable(subclass.predict) or
                NotImplemented)

    @abc.abstractmethod
    def load_model(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def predict(self, image):
        """Extract text from the data set"""
        raise NotImplementedError