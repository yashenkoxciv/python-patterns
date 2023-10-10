class Logger:
    _instance = None

    # WARNING: not define init dunder method to avoid re-initialization 
    # def __init__(self):
    #     pass

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super().__new__(cls)

            # initializing
            cls._instance.field = 'value'
        return cls._instance