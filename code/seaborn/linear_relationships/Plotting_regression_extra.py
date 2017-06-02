import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")


sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg");
