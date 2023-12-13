from abc import ABC, abstractmethod

from scipy.stats import cauchy
class Estimation(ABC):
  @abstractmethod
  def estimate(sample):
    pass


import statistics

import numpy as np

class Mean(Estimation):
  def estimate(self, sample):
    return statistics.mean(sample)


class Choose_Mean(Estimation):
  def estimate(self, sample, *args, **kwargs):
    return np.median(sample)


class Cauchy_Estimate(Estimation):
  def estimate(self, sample, *args, **kwargs):
    return cauchy.fit(sample)


class Var(Estimation):
  def estimate(self, sample):
    return statistics.variance(sample)