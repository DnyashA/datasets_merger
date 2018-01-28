import pandas as pd
import numpy as np

class Splitter:

    def split(self, test_percent, dataset, columns):
        np.random.shuffle(dataset)
        train_index = int(dataset.shape[0] * (1 - test_percent) - 1)
        test_index = int(dataset.shape[0] * test_percent)
        train = pd.DataFrame(dataset[train_index:], columns=columns)
        test = pd.DataFrame(dataset[-test_index:], columns=columns)
        return train, test