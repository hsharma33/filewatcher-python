from src.Observable import Observerable
from src.Observer import Observer

# import sys, os
# sys.append(os.path.realpath.append(".."))

# Objective: to test if the given function is triggered by the object calling the observer. 
def test_add():
    user_code = Observer()
    assert Observerable().add(user_code)


# Objective: to test if the given function is triggered by the object calling the observer. 
def test_remove():
    assert Observerable().remove()


# Objective: to test if the given function is triggered by the object calling the observer. 
def test_notify():
    assert Observerable().notify()
