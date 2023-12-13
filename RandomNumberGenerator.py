from abc import  ABC, abstractmethod
from  RandomVariable import RandomVariable


class RandomNumberGenerator(ABC):
  def __init__(self, random_variable: RandomVariable):
    self.random_variable = random_variable

  @abstractmethod
  def get(self, N):
    pass