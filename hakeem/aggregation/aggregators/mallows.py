import numpy as np
import pandas as pd

from hakeem.aggregation.base import WeightedAggregator


class StandardApprovalAggregator(WeightedAggregator):
    def compute_weights(self, annotations: pd.DataFrame) -> pd.Series:
        return pd.Series(1, index=annotations.index)


class EuclidAggregator(WeightedAggregator):
    def compute_weights(self, annotations: pd.DataFrame) -> pd.Series:
        vote_size = annotations.sum(axis=1)
        assert np.all(vote_size > 0), "Euclid weights are not defined for empty votes."
        return np.sqrt(vote_size + 1) - np.sqrt(vote_size - 1)


class JaccardAggregator(WeightedAggregator):
    def compute_weights(self, annotations: pd.DataFrame) -> pd.Series:
        vote_size = annotations.sum(axis=1)
        assert np.all(vote_size > 0), "Jaccard weights are not defined for empty votes."
        return 1 / vote_size


class DiceAggregator(WeightedAggregator):
    def compute_weights(self, annotations: pd.DataFrame) -> pd.Series:
        vote_size = annotations.sum(axis=1)
        return 2 / (vote_size + 1)
