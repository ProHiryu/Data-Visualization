import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")

# can reshape the size of graph
f, ax = plt.subplots(figsize=(5, 6))
sns.regplot(x="total_bill", y="tip", data=tips, ax=ax)

# use size and aspect can also set the shape
# size is the size of graph,aspect is the width/height
sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           col_wrap=2, size=3)
sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           col_wrap=2, size=4)
sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           aspect=.5)
sns.lmplot(x="total_bill", y="tip", col="day", data=tips,
           aspect=.2)

sns.plt.show()
