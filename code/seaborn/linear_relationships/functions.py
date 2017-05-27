import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")

# the shape is not equal, and accept pandas and numpy
sns.regplot(x="total_bill", y="tip", data=tips);

# the shape is equal rectangular
sns.lmplot(x="total_bill", y="tip", data=tips);

# add some noise to make discrete plot more clear(it does not influence the data)
sns.lmplot(x="size", y="tip", data=tips, x_jitter=.05);

# collapse over the observations in each discrete bin
sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean);

sns.plt.show()
