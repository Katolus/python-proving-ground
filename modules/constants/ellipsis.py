from typing import Callable
from typing import Tuple


print(f"Ellipsis literal can represented by ... and Ellipsis variables")
print(...)
print(Ellipsis)


print("Arbitrary-length homogeneous tuples can be expressed using one type and ellipsis ->",
      Tuple[int, ...])


print("An Ellipsis is a placeholder for unwritten code and can be used to define return \n type of a callable without specifying the call signature of the list of arguments")


def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    # Body
    ...


print("""
def partial(func: Callable[..., str], *args) -> Callable[..., str]:
    # Body
    ...
""")

print(partial(lambda x: x+1))
print(partial(lambda x, y: print(x, y)))
