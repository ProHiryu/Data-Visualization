import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")

# plot depends on the smoker distribute ['Yes','No']
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips);

# use different scatterplot markers (different palette means the default color is different)
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
           markers=["o", "x"], palette="Set1");

# plot depends on the time distribute ['lunch','dinner'] (separate into two graphs)
sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips);

# plot depends on the time and sex distribute (separate into four graphs)
sns.lmplot(x="total_bill", y="tip", hue="smoker",
           col="time", row="sex", data=tips);

sns.plt.show()
