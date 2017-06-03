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


# boxplot
sns.boxplot(x="day", y="total_bill", hue="time", data=tips);

# violinplot
sns.violinplot(x="total_bill", y="day", hue="time", data=tips);

# add some complexity relative to the straightforward boxplot
sns.violinplot(x="total_bill", y="day", hue="time", data=tips,
               bw=.1, scale="count", scale_hue=False);

# split boxplot into two part count on "sex"(comparance of the two pair data)
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True);
