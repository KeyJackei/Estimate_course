from abc import ABC, abstractmethod


class RandomVariable(ABC):
  @abstractmethod
  def pdf(self, x):
    pass

  @abstractmethod
  def cdf(self, x):
    pass

  @abstractmethod
  def quantile(self, alpha):
    pass