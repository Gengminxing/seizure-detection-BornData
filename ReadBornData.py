# coding=utf-8
# usr/bin/env python

"""
Author: Geng Minxing
Email: gengminxing1995@163.com
Date: 2019/7/29 10:00
"""
import numpy as np


class load_seizure_data():
    def __init__(self):
        self.task = 0  # Default task
        self.task_list = (0, 1, 2)
        self.feature_extraction = "Raw_Data"  # Default feature
        self.feature_list = (
            "Raw_Data",
            "PSD",
            "Time_Estimate",
            "Wavelet_Coff",
            "STFT_SVD")
        self.class_list = ['A', 'B', 'C', 'D', 'E']

    def run(self, n_task, n_feature, data_path):
        if n_task in self.task_list:
            self.task = n_task
        else:
            raise ValueError("The task number must be in (0, 1, 2)")
        if n_feature in self.feature_list:
            self.feature_extraction = n_feature
        else:
            raise ValueError(
                "The feature extraction must be in ('Raw_Data', 'PSD', "
                "'Time_Estimate', 'Wavelet_Coff', 'STFT_SVD') ")
        data, label = self.get_class_data(data_path)
        extra_data = self.get_feature_data(data)
        return extra_data, label

    def get_class_data(self, data_path):
        origin_data = []
        for name in self.class_list:
            load_name = name + '.npz'
            npz_file = np.load(data_path + load_name)
            load_data = npz_file['arr_0']
            origin_data.append(load_data)

        # 根据任务读取数据, 0: ABvsCDvsE, 1: ABCDvsE, 2: ABvsCD
        if self.task == 0:
            read_data = np.concatenate(
                (origin_data[0],
                 origin_data[1],
                 origin_data[2],
                 origin_data[3],
                 origin_data[4]),
                axis=0)
            read_label = np.zeros((read_data.shape[0],), dtype=np.int)
            read_label[200:400] = 1
            read_label[400:] = 2
            return read_data, read_label
        elif self.task == 1:
            read_data = np.concatenate(
                (origin_data[0],
                 origin_data[1],
                 origin_data[2],
                 origin_data[3],
                 origin_data[4]),
                axis=0)
            read_label = np.zeros((read_data.shape[0],), dtype=np.int)
            read_label[:400] = 0
            read_label[400:] = 1
            return read_data, read_label
        elif self.task == 2:
            read_data = np.concatenate(
                (origin_data[0], origin_data[1], origin_data[2], origin_data[3]), axis=0)
            read_label = np.zeros((read_data.shape[0],), dtype=np.int )
            read_label[:200] = 0
            read_label[200:] = 1
            return read_data, read_label
        else:
            raise AttributeError("The task number must be in (0, 1, 2)")

    def get_feature_data(self, seizure_data):
        if self.feature_extraction == "Raw_Data":
            return seizure_data
        elif self.feature_extraction == "PSD":
            return seizure_data
        elif self.feature_extraction == "Time_Estimate":
            return seizure_data
        elif self.feature_extraction == "Wavelet_Coff":
            return seizure_data
        elif self.feature_extraction == "STFT_SVD":
            return seizure_data


if __name__ == '__main__':
    rd = load_seizure_data()
    data, label = rd.run(0, "PSD", 'E:/Pycharm_project/MachineLearning/BornData/')
