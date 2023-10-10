import random
import patterns.singleton_module as singleton_1
import patterns.singleton_module as singleton_2


def test_class_objects():
    # every import of a module uses the same object of the module
    # so class Logger is created only once
    assert singleton_1.Logger is singleton_2.Logger
    assert id(singleton_1.Logger) == id(singleton_2.Logger)


def test_class_instances():
    # logger object is also created only once (when first import happens)
    assert singleton_1.logger is singleton_2.logger
    assert id(singleton_1.logger) == id(singleton_2.logger)


def test_instance_field():
    assert singleton_1.logger.field == singleton_2.logger.field


def test_instance_field_change():
    singleton_1.logger.field = random.randint(0, 9)
    assert singleton_1.logger.field == singleton_2.logger.field
