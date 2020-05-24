from src.IObservable import IObservable
import time

class Observable(IObservable):

    def __init__(self):
        self.observers_dict = {}  
        

    def add(self, Observer):
        
        self.observers_dict[Observer.hash_all_files] = Observer

    def remove(self, files_hash):
        del self.observers_dict[files_hash]

    def notify(self):
        for k,v in self.observers_dict.items():
            v.trigger()

    def has_something_changed(self, hash_value):
        
        return not self.observers_dict.get(hash_value,False)
    
    def clear_observer_dict(self):
        self.observers_dict.clear()
