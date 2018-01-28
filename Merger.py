import glob
import os

import csv
import pandas as pd
import numpy as np
import shutil

from PathContainer import DefaultPathes as def_pt
from Splitter import Splitter

class Merger(object):

    def __init__(self, pathes, npy=False, shuffle=False, split=False):
        # Path to standard dataset
        self.main_dataset_path = pathes[def_pt.main_dat_path]
        # Path to dataset which should be merged with standard
        self.sub_dataset_path = pathes[def_pt.sub_dat_path]
        # Standard .csv file with markup
        self.main_markup = pathes[def_pt.main_markup]
        # .csv file which should be merged with standard
        self.sub_markup = pathes[def_pt.sub_markup]
        # Path to save merged dataset
        self.save_path = pathes[def_pt.save_path]
        # True for save dataset as NumPy archive (default False)
        self.npy = npy
        # True for shuffle merged dataset (default False)
        self.shuffle = shuffle
        # True for split merged dataset to train and test (default False)
        self.split = split
        self.main_data = []
        self.sub_data = []
        self.main_cts = []
        self.sub_cts = []

        if not os.path.exists(self.save_path):
            os.makedirs(str(self.save_path))
        if not os.path.exists(str(self.save_path) + 'images/'):
            os.makedirs(str(self.save_path) + 'images/')
        if not os.path.exists(str(self.save_path) + 'csv_files/'):
            os.makedirs(str(self.save_path) + 'csv_files/')

    def collect_csv(self):
        with open(str(self.main_dataset_path) + str(self.main_markup)) as maindata:
            # Delimiter have to be specified depending on csv content
            reader = csv.reader(maindata, delimiter=',')
            for row in reader:
                self.main_data.append(row)
        with open(str(self.sub_dataset_path) + str(self.sub_markup)) as subdata:
            # Delimiter have to be specified depending on csv content
            reader = csv.reader(subdata, delimiter=';')
            for row in reader:
                self.sub_data.append(row)

    def collect_ct(self):
        # CT's extension have to be specified (usualy it's .raw or .dicom)
        self.main_cts = glob.glob(str(self.main_dataset_path) + '**/*.raw', recursive=True)
        self.sub_cts = glob.glob(str(self.sub_dataset_path) + '**/*.raw', recursive=True)

    def merge(self):
        self.collect_csv()
        main_dataset = pd.DataFrame(self.main_data[1:], columns=self.main_data[0])
        main_dataset = main_dataset.loc[:, ~main_dataset.columns.duplicated()]
        sub_dataset = pd.DataFrame(self.sub_data[1:], columns=self.sub_data[0])
        sub_dataset = sub_dataset.loc[:, ~sub_dataset.columns.duplicated()]
        result_dataset = main_dataset.append(sub_dataset, ignore_index=True)
        pd.DataFrame.to_csv(result_dataset, str(self.save_path) + 'csv_files/result_dataset.csv')
        for path in self.main_cts:
            shutil.copy(path, str(self.save_path) + 'images')
        for path in self.sub_cts:
            shutil.copy(path, str(self.save_path) + 'images')

        if self.shuffle:
            shuffled = pd.DataFrame(pd.DataFrame.as_matrix(result_dataset), columns=result_dataset.columns)
            np.random.shuffle(pd.DataFrame.as_matrix(shuffled))
            pd.DataFrame.to_csv(shuffled, str(self.save_path) + 'csv_files/result_dataset_shuffled.csv')

        if self.npy:
            result_dataset_npy = pd.DataFrame.as_matrix(result_dataset)
            np.save(str(self.save_path) + 'result_dataset.npy', result_dataset_npy)

        if self.split:
            train, test = Splitter.split(0.1, pd.DataFrame.as_matrix(result_dataset), result_dataset.columns)
            pd.DataFrame.to_csv(train, str(str(self.save_path) + 'csv_files/result_dataset_train.csv'))
            pd.DataFrame.to_csv(test, str(str(self.save_path) + 'csv_files/result_dataset_test.csv'))
