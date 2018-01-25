from binance.client import Client
import numpy as np


def choose_random_pair(pairs, K):
	chosen_pair_idx = np.random.rand(K)*len(pairs)
	return [pairs[int(idx)] for idx in chosen_pair_idx]
