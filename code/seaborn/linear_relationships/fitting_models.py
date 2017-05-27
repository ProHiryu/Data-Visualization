import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "regression")))
tips = sns.load_dataset("tips")
anscombe = sns.load_dataset("anscombe")

# the linear model to fit
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80})
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           ci=None, scatter_kws={"s": 80})

# fit a polynomial regression model
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),
           order=2, ci=None, scatter_kws={"s": 80})

# uses a different loss function to downweight relatively large residuals(get out of outliers)
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'III'"),
           robust=True, ci=None, scatter_kws={"s": 80})

# use logistic regression
tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           y_jitter=.03);
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03)

# calculate the intensive data
sns.lmplot(x="total_bill", y="tip", data=tips,
           lowess=True);

# 计算简单线性回归的误差，如果每个点的误差在y=0附近移动，那么适合简单线性回归
fig1 = plt.figure() ## new figure to plot in a new figure
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});

fig2 = plt.figure()
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'II'"),order=2,
              scatter_kws={"s": 80});

sns.plt.show()
