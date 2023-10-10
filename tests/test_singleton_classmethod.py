import pytest
import random
from patterns import singleton_classmethod as singleton_1
from patterns import singleton_classmethod as singleton_2


def test_class_objects():
    # every import of a module uses the same object of the module
    # so class Logger is created only once
    assert singleton_1.Logger is singleton_2.Logger
    assert id(singleton_1.Logger) == id(singleton_2.Logger)


def test_class_instances():
    # logger object is also created only once (when first import happens)
    logger_1 = singleton_1.Logger.instance()
    logger_2 = singleton_2.Logger.instance()
    assert logger_1 is logger_2
    assert id(logger_1) == id(logger_2)


def test_instance_field():
    logger_1 = singleton_1.Logger.instance()
    logger_2 = singleton_2.Logger.instance()
    assert logger_1.field == logger_2.field


def test_instance_field_change():
    logger_1 = singleton_1.Logger.instance()
    logger_1.field = random.randint(0, 9)
    logger_2 = singleton_2.Logger.instance()
    assert logger_1.field == logger_2.field


def test_exception_call_instance_instead():
    with pytest.raises(RuntimeError):
        logger_1 = singleton_1.Logger()


def test_instance_field_and_instance():
    logger_1 = singleton_1.Logger.instance()
    logger_2 = singleton_2.Logger.instance()
    assert logger_1 is singleton_2.Logger._instance
    assert logger_2 is singleton_1.Logger._instance


