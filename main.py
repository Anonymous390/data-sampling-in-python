import plotly.figure_factory as ff
from statistics import *
import random
import pandas as pd

df = pd.read_csv("test.csv")
data = df["temperature"].tolist()

population_mean = mean(data)

standard_deviation = stdev(data)
print(standard_deviation)

def random_set_of_mean(counter):
    dataset= []

    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    sample_mean = mean(dataset)
    return sample_mean

def setup():
    mean_list = []

    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)

    plot_graph(mean_list)

def plot_graph(mean_list):
    df = mean_list
    fig = ff.create_distplot([mean_list], ["temperature"])
    fig.show()

setup()
