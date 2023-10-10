class Person:
    def __new__(cls):
        print('Run __new__ method')
        self = super().__new__(cls)
        return self
    
    def __init__(self):
        print('Run __init__ method')


if __name__ == '__main__':
    person = Person()

    # Output will be:
    # Run __new__ method
    # Run __init__ method