from src.Observable import Observable
from src.Observer import Observer
import time
import glob
import json
import os
import _sha256
import hashlib
# Python 3.7+

if __name__ == "__main__":


    observable = Observable()
    
    with open('config.json') as f:
            configuration = json.load(f)
    
    def repl():
        
        while True:
            observer = construct_observer()
            hash_val = observer.hash_all_files
            if observable.has_something_changed(observer.hash_all_files):
                observable.clear_observer_dict()
                observable.add(observer)
                observable.notify()
            
            time.sleep(configuration["sleep_time_s"])

    
    def construct_observer():
    
        observer = Observer()
        hash_list = []
        
        include_directories = configuration["include"]
        for this_file_path in glob.glob(include_directories +"**/*.*", recursive=True):
            fparam = str(os.stat(this_file_path))
            fparam = fparam.encode("UTF-8")
            hasher = hashlib.sha256()
            hasher.update(fparam)
            fhash = str(hasher.digest())
            hash_list.append(fhash)
        observer.hash_all_files = "|".join(hash_list)
        return observer        
    
    repl()