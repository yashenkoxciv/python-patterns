class Logger:
    _instance = None

    def __init__(self) -> None:
        raise RuntimeError('Call instance() instead')
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)

            # initializing
            cls._instance.field = 'value'
        return cls._instance