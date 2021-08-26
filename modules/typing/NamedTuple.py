# Typed namedtuple
from typing import NamedTuple

class Employee(NamedTuple):
    """Represents an employee."""
    name: str
    id: int = 3

employee = Employee('Patrick', 2)
print(employee)
print(employee.__annotations__)
print(employee.__doc__)

# Another way to represent typed named tuples
Police = NamedTuple('Police', [('unit', str), ('id', dict)])
police_man = Police('Emping', 24)
print(police_man)
print(police_man.__annotations__)
print(police_man.__doc__)