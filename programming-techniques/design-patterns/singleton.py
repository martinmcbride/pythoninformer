# Author:  Martin McBride
# Created: 2021-09-01
# Copyright (C) 2021, Martin McBride
# License: MIT

# Examples of different implementations of logger.
# Each example is contained withing a function to provide a different namespace

def logger_class():
    # Simple logger class that isn't a singleton

    class Logger():

        # This isn't really needed, just illustrates default __new__
        def __new__(cls, *args, **kwargs):
            return super(Logger, cls).__new__(cls, *args, **kwargs)

        def message(self, str):
            # Log the message
            print(str)


    a = Logger()
    b = Logger()
    print(a is b)


def singleton_logger_class():
    # Simple singleton logger class using __new__

    class Logger():
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            return cls._instance

        def message(self, str):
            # Log the message
            print(str)


    a = Logger()
    b = Logger()
    print(a is b)

def singleton_logger_initialize_class():
    # Singleton class with initializer

    class Logger():
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            return cls._instance

        def initialize(self):
            # Initialize the logger
            ...

        def message(self, str):
            # Log the message
            print(str)


    Logger().initialize()
    a = Logger()
    b = Logger()
    print(a is b)

def singleton_logger_base_class():
    # Singleton using a base class

    class Singleton():
        _instance = None

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
            return cls._instance


    class Logger(Singleton):

        def message(self, str):
            # Log the message
            print(str)


    a = Logger()
    b = Logger()
    print(a is b)

def singleton_factory_method_logger_class():
    # Simple logger class that isn't a singleton

    class Logger():

        def message(self, str):
            # Log the message
            print(str)

    def get_logger(logger=Logger()):
        return logger


    a = get_logger()
    b = get_logger()
    print(a is b)



logger_class()
singleton_logger_class()
singleton_logger_initialize_class()
singleton_logger_base_class()
singleton_factory_method_logger_class()