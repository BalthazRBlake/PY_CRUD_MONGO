from dataclasses import dataclass

@dataclass
class K9:
  def __init__(self, k9_name: str, age: int, nature: str, birth_day: str):
    self.k9_name = k9_name
    self.age = age
    self.nature = nature
    self.birth_day = birth_day
    
  def __str__(self):
    return f"{{'k9_name': '{self.k9_name}', 'age': '{self.age}','nature': '{self.nature}','birth_day': '{self.birth_day}'}}"