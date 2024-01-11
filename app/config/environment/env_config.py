from abc import ABC, abstractmethod

class EnvConfig():
    
    def __init__(self) -> None:
        self._check()
        self.print_info()

    def _check(self):
        is_valid = True
        for key, val in vars(self).items():
            if val is None:
                is_valid = False
                print(f">>> Initialization error: [{key}] is not set")        

        if (not is_valid):
            raise RuntimeError(">>> Application configuration error")

    @abstractmethod    
    def print_info(self):
        pass