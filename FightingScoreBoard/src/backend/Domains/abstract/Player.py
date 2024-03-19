import abc

class Player(abc.ABC):
    name
    country
    tag
    character
    sponsor
    wincounter
    
    @abc.abstractmethod
    def GetFullName(self):
        return self.tag + " | " + self.name
        
    