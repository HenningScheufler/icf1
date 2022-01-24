# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


freeSurf_min_max = pd.read_csv("results/freeSurf_min_max.csv")

sns.lineplot(x='t', y='min', hue='var_0', data=freeSurf_min_max)
plt.savefig("results/freeSurf_min.png")

plt.figure()
sns.lineplot(x='t', y='max', hue='var_0', data=freeSurf_min_max)
plt.savefig("results/freeSurf_max.png")

plt.show()
