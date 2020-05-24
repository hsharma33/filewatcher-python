from src.Observer import Observer
# import sys, os
# sys.append(os.path.realpath.append(".."))

# Objective: to test if the given function is triggered by the object calling the observer. 
def test_trigger():
    assert Observer().trigger() == None