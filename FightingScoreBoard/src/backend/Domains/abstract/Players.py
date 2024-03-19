import abc

class PlayersInformation(abc.ABC):
    Players = []
    RoundName
    RoundNumber
    
    @abc.abstractmethod
    def Swap(self) : self
    
    @abc.abstractmethod
    def Clear(self) : self
    
    @abc.abstractmethod
    def CharSwap(self) : self
    
    @abc.abstractmethod
    def NameSwap(self) : self
    
    @abc.abstractmethod
    def WinLoseSwap(self) : self