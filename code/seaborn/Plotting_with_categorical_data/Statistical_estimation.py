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

# barplot show the mean in each categories(black line is the a confidence interval around the estimate and plots that using error bars)
sns.barplot(x="sex", y="survived", hue="class", data=titanic);

# count in each categories
sns.countplot(x="deck", data=titanic, palette="Greens_d");

# use hue
sns.countplot(y="deck", hue="class", data=titanic, palette="Greens_d");

sns.plt.show()
