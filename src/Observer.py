from src.IObserver import IObserver

from src.trigger_script import my_custom_script

class Observer(IObserver):


    def trigger(self):
        my_custom_script()
        

    def __init__(self):
        self.hash_all_files = None
        