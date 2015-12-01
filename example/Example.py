class Animal:
    initial = None

    def __new__(cls, *args, **kwargs):
        if cls.initial is None:
            cls.initial = super(Animal, cls).__new__(cls)
        return cls.initial

    def __init__(self):
        self.cat = "barsik"


animal = Animal()
print(Animal().cat)