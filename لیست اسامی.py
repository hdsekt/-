class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

people = [
    Person('Raj', 'Nayyar'),
    Person('Suraj', 'Sharma'),
    Person('Karan', 'Kumar'),
    Person('Jade', 'Canary'),
    Person('Raj', 'Thakur'),
    Person('Raj', 'Sharma'),
    Person('Kiran', 'Kamla'),
    Person('Armaan', 'Kumar'),
    Person('Jaya', 'Sharma'),
    Person('Ingrid', 'Galore'),
    Person('Jaya', 'Seth'),
    Person('Armaan', 'Dadra'),
    Person('Ingrid', 'Maverick'),
    Person('Aahana', 'Arora')
]

# مرتب سازی بر اساس اسم و نام خانوادگی
sorted_people = sorted(people, key=lambda person: (person.last_name, person.first_name))

for person in sorted_people:
    print(person)