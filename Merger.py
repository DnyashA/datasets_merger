import csv
import pandas as pd
from Splitter import Splitter
import glob
import os
import numpy as np

class Merger(object):

    def __init__(self, main_dat_path, sub_dat_path, save_path, npy=False, shuffle=False, split=False):
        # Path to standard dataset
        self.main_dataset_path = main_dat_path
        # Path to dataset which should be merged with standard
        self.sub_dataset_path = sub_dat_path
        # Path to save merged dataset
        self.save_path = save_path
        # True for save dataset as NumPy archive (default False)
        self.npy = npy
        # True for shuffle merged dataset (default False)
        self.shuffle = shuffle
        # True for split merged dataset to train and test (default False)
        self.split = split
        self.main_data = []
        self.sub_data = []

        if not os.path.exists(self.save_path):
            os.makedirs(str(self.save_path))

    def collect_csv(self):
        with open(self.main_dataset_path) as maindata:
            # Delimiter have to be specified depending on csv content
            reader = csv.reader(maindata, delimiter=',')
            for row in reader:
                self.main_data.append(row)
        with open(self.sub_dataset_path) as subdata:
            # Delimiter have to be specified depending on csv content
            reader = csv.reader(subdata, delimiter=';')
            for row in reader:
                self.sub_data.append(row)

    def merge(self):
        main_dataset = pd.DataFrame(self.main_data[1:], columns=self.main_data[0])
        main_dataset = main_dataset.loc[:, ~main_dataset.columns.duplicated()]
        sub_dataset = pd.DataFrame(self.sub_data[1:], columns=self.sub_data[0])
        sub_dataset = sub_dataset.loc[:, ~sub_dataset.columns.duplicated()]
        result_dataset = main_dataset.append(sub_dataset, ignore_index=True)
        pd.DataFrame.to_csv(result_dataset, str(self.save_path) + 'result_dataset.csv')

        if self.shuffle:
            shuffled = pd.DataFrame(pd.DataFrame.as_matrix(result_dataset), columns=result_dataset.columns)
            np.random.shuffle(pd.DataFrame.as_matrix(shuffled))
            pd.DataFrame.to_csv(shuffled, str(self.save_path) + 'result_dataset_shuffled.csv')

        if self.npy:
            result_dataset_npy = pd.DataFrame.as_matrix(result_dataset)
            np.save(str(self.save_path) + 'result_dataset.npy', result_dataset_npy)

        if self.split:
            s = Splitter()
            train, test = s.split(0.1, pd.DataFrame.as_matrix(result_dataset), result_dataset.columns)
            pd.DataFrame.to_csv(train, str(str(self.save_path) + 'result_dataset_train.csv'))
            pd.DataFrame.to_csv(test, str(str(self.save_path) + 'result_dataset_test.csv'))
