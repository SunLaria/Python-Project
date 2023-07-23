class Task:
    def __init__(self, name = "default", creation_date = "default", end_date = "default", responsible_person = "default", description ="default", category = "default"):
        self.name = name
        self.creation_date = creation_date
        self.end_date = end_date
        self.responsible_person = responsible_person
        self.description = description
        self.category = category
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name
    
    def taskinfo(self) -> str:
        return self.name, self.creation_date, self.end_date, self.responsible_person, self.description, self.category
    