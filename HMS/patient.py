class Patient:
    name = None
    age = None
    id = None
    def __init__(self, name, age, id):
        self.name = name
        self.age = int(age)
        self.id = id