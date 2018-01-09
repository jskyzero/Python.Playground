""" Try1.py
    One Lab About date process
    By jzkysero
"""
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PIL import Image


class Try1(object):
    """Try1 Class"""

    def __init__(self):
        """initial data_url and read data"""
        self.data_url = ""
        self.data = ""
        self.defaule_initial()

    def main(self):
        self.job4()

    def defaule_initial(self):
        """defaule config"""
        default_url = "https://raw.githubusercontent.com/alstat/Analysis-with-Programming/master/2014/Python/Numerical-Descriptions-of-the-Data/data.csv"
        self.set_data_url(default_url)
        self.read_data_csv()

    def read_data_csv(self):
        """read data form url"""
        self.data = pd.read_csv(self.data_url)

    def set_data_url(self, url):
        """set data url"""
        self.data_url = url

    def job1(self):
        """part 1"""
        print "data.head()"
        print self.data.head()
        print "data.tail()"
        print self.data.tail()
        print "data.columns"
        print self.data.columns
        print "data.index"
        print self.data.index
        print "data.T.head()"
        print self.data.T.ix[0:2, 0:10:2]
        print "[1:10:2,0:2]"
        print self.data.ix[0:10:2, 0:2]
        # axix = 0 raw
        # axix = 1 column
        print "data.column[[1,2]]"
        print self.data.columns[[1, 2]]
        print self.data.drop(self.data.columns[[1]], axis=1).head()
        print "data.describe()"
        print self.data.describe()

    def job2(self):
        print ss.ttest_1samp(a=self.data.ix[:, "Abra"], popmean=15000)

    def job3(self):
        plt.style.use("ggplot")
        # can also be {line,bar}
        plt.show(self.data.plot(kind="box"))

    def job4(self):
        # from
        # http://bookshadow.com/weblog/2015/11/21/sklearn-kmeans-captcha-character-cut/
        im = np.array(Image.open("docs/zftb-original.gif"))
        h, w = im.shape
        X = [(h - x, y) for x in range(h) for y in range(w) if im[x][y]]
        X = np.array(X)
        n_clusters = 4
        k_means = KMeans(init='k-means++', n_clusters=n_clusters)
        k_means.fit(X)
        k_means_labels = k_means.labels_
        k_means_cluster_centers = k_means.cluster_centers_
        k_means_labels_unique = np.unique(k_means_labels)
        colors = ['#4EACC5', '#FF9C34', '#4E9A06', '#FF3300']
        plt.figure()
        plt.hold(True)
        for k, col in zip(range(n_clusters), colors):
            my_members = k_means_labels == k
            cluster_center = k_means_cluster_centers[k]
            plt.plot(X[my_members, 1], X[my_members, 0], 'w',
                     markerfacecolor=col, marker='.')
            plt.plot(cluster_center[1], cluster_center[0], 'o', markerfacecolor=col,
                     markeredgecolor='k', markersize=6)
        plt.title('KMeans')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    Try = Try1()
    Try.main()
