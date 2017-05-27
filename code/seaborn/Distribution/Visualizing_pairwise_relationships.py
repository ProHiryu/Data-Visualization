import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

# the normal plot of pair dataset
sns.pairplot(iris);

# use kde to plot pair dataset(the default camp is green,but the line is blue)
g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot, cmap="Blues_d", n_levels=6);

sns.plt.show()
