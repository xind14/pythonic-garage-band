class Musician:
   count =0
   def __str__(self,name='unknown'):
      self.name=name
      Musician.count+=1


class Guitarist(Musician):
    def __init__(self, name='unknown'):
      self.name=name

    def __str__(self):
      return  f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
       return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
       return f'guitar'
    
    def play_solo(self):
        return f"face melting guitar solo"

   

class Drummer(Musician):
    def __init__(self, name='unknown'):
       self.name=name
    
    def __str__(self):
       return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
       return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
       return f'drums'
    
    def play_solo(self):
        return f"rattle boom crash"

class Bassist(Musician):
    def __init__(self, name='unknown'):
       self.name=name
    
    def __str__(self):
       return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
       return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
      return f'bass'
    
    def play_solo(self):
      return f"bom bom buh bom"
    

class Band:
    instances=[]

    def __init__(self, name, members=[]):
       self.name=name
       self.members=members
       self.instances.append(self) 
       
    def instruments(self):
       return [member.get_instrument()for member in self.members]
    

    def play_solos(self):
       return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
       return cls.instances
       