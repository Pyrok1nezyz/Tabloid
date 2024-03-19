import abc

class Meta(abc.ABC):
    commentators = []
    fightrule 
    notation
    sponsor
    prizepool
    title
    url
    PlayersCount # Количество игроков в турнире
    
    @abc.abstractmethod
    def ResetInformation(self): self
    
    @abc.abstractmethod
    def Swap(self): self
        
        
    