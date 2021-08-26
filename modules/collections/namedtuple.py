from collections import namedtuple

Car = namedtuple("Car", "Price Mileage Colour Class")
car = Car(Price=100000, Mileage=30, Colour="Cyan", Class="Y")
print(car)

Person = namedtuple("Person", ["name", "height"], defaults=['John', 152])
person = Person("John", 124)
print(person)

print("_doc of person -> ", person.__doc__)
print("_fields of person -> ", person._fields)
print("_field_defaults of person", person._field_defaults)


# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

# Dict into a namedtuple
d = {"x": 1, "y": 2}
p = Point(**d)

# >>> class Point(namedtuple('Point', ['x', 'y'])):
# ...     __slots__ = ()
# ...     @property
# ...     def hypot(self):
# ...         return (self.x ** 2 + self.y ** 2) ** 0.5
# ...     def __str__(self):
# ...         return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

# >>> for p in Point(3, 4), Point(14, 5/7):
# ...     print(p)
# Point: x= 3.000  y= 4.000  hypot= 5.000
# Point: x=14.000  y= 0.714  hypot=14.018

# Interesting!
# The subclass shown above sets `__slots__` to an empty tuple.
# This helps keep memory requirements low by preventing the creation of instance dictionaries.

print("instantiate with positional or keyword arguments", p)

print("indexable like the plain tuple (%d, %d) -> p[0] + p[1]", p[0], p[1])

x, y = p
print("unpack like a regular tuple x, y = p ", x, y)

print("fields are accesible by name", p.x,  p.y)


# Docstrings can be customized by making direct assignments to the __doc__ fields:

Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'

book = Book(1, 'Title', 'Author')
print(book.__doc__)

# For types see NamedTuple.py