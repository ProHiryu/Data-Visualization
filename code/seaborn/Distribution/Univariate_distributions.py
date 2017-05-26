import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)

x = np.random.normal(size=100)

# normal histogram with KDE(kernel density estimate)
sns.distplot(x)

# plot without kde
sns.distplot(x, kde=False, rug=True);

# plot without hist
sns.distplot(x, hist=False, rug=True);

# the width of each hist,bins grows,the width get down
sns.distplot(x, bins=20, kde=False, rug=True);


sns.kdeplot(x, shade=True);

sns.kdeplot(x)
sns.kdeplot(x, bw=.2, label="bw: 0.2")
sns.kdeplot(x, bw=2, label="bw: 2")
plt.legend();

sns.distplot(x, kde=False, fit=stats.gamma);

sns.plt.show()
