import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True)

np.random.seed(sum(map(ord, "categorical")))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# simple
sns.stripplot(x="day", y="total_bill", data=tips);

# use jitter to see the distribution
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True);

# to avoid overlap
sns.swarmplot(x="day", y="total_bill", data=tips);

# add a nested categorical variable with the hue parameter
sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips);

# change x and y (use orient[orient = ['v','h']] to set the orientation)
sns.swarmplot(x="total_bill", y="day", hue="time", data=tips);


sns.plt.show()
