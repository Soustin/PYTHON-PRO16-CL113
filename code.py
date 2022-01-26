#Importing the important modules
import pandas as pd
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import scipy.stats as stats
import csv

#Plotting the graph
df = pd.read_csv("savings_data_final.csv")
fig1 = px.scatter(df, y="quant_saved", color="rem_any")
# fig1.show()

with open('savings_data_final.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

import seaborn as sns

sns.boxplot(data = df, x = df["quant_saved"])

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3-q1
print(f"IQR of Quantity saved is {iqr}")
lowerWhisker = q1-1.5*iqr
upperWhisker = q3+1.5*iqr
print(f"Upper Whisker of Quantity saved is {upperWhisker}")
print(f"Lower Whisker of Quantity saved is {lowerWhisker}")

new_df = df[df["quant_saved"]<upperWhisker]

#Mean, median and mode of savings
all_savings_new = new_df["quant_saved"].tolist()

print(f"Mean of savings without outliers - {statistics.mean(all_savings_new)}")
print(f"Median of savings without outliers - {statistics.median(all_savings_new)}")
print(f"Mode of savings without outliers - {statistics.mode(all_savings_new)}")
print(f"Standard deviation in savings without outliers - {statistics.stdev(all_savings_new)}")

fig4 = ff.create_distplot([new_df["quant_saved"].tolist()], ["Savings"], show_hist=False)
# fig4.show()

#Collecting 1000 samples of 100 data points each, saving their averages in a list
import random

sampling_mean_list = []
for i in range(1000):
  temp_list = []
  for j in range(100):
    temp_list.append(random.choice(all_savings_new))
  sampling_mean_list.append(statistics.mean(temp_list))

mean_sampling = statistics.mean(sampling_mean_list)

fig5 = ff.create_distplot([sampling_mean_list], ["Savings (Sampling)"], show_hist=False)
fig5.add_trace(go.Scatter(x=[mean_sampling, mean_sampling], y=[0, 0.1], mode="lines", name="MEAN"))
fig5.show()

print(f"Standard Deviation of the sampling data - {statistics.stdev(sampling_mean_list)}")

print(f"Population Mean - {statistics.mean(all_savings_new)}")

print(f"Sampling Distribution Mean - {mean_sampling}")

#temp_df will have the rows where age is not 0
temp_df = new_df[new_df.age != 0]

age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")
zscore = stats.zscore(all_savings_new)
print(f"Zscore = {zscore}")