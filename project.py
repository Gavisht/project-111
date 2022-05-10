from cv2 import trace
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("project1.csv")
data = df["reading_time"].tolist()

#plotting the graph
# fig = ff.create_distplot([data],["Math Scores"], show_hist= False)
# fig.show()

#calculating the mean and standard deviation of the population data
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

# print("mean of popultion:- ",mean)
# print("Standard deviation of popultion:- ",std_deviation)



##  code to find the mean of 100 data points 1000 times 
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean



# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

df = pd.read_csv("project2.csv")
data = df["reading_time"].tolist()
mean1 = statistics.mean(data)
print(mean1)
fig = ff.create_distplot([mean_list],["reading_time"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,1],mode = "lines",name = "mean"))
fig.show()
zscore = (mean - mean1)/std_deviation
print(zscore)
