import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

# the enhance of plt.scatter()
sns.jointplot(x="x", y="y", data=df);

# Hexbin plots
x, y = np.random.multivariate_normal(mean, cov, 1000).T
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k");

# Kernel density estimation
sns.jointplot(x="x", y="y", data=df, kind="kde");

sns.plt.show()
