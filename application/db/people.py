class Employee():
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname

    def get_employees(self):
        print(f'Hello, {self.name} {self.surname} (from people.py)')
