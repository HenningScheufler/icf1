# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


freeSurf_min_max = pd.read_csv("results/freeSurf_min_max.csv")

sns.lineplot(x='t', y='min', hue='solver', data=freeSurf_min_max)
plt.savefig("results/freeSurf_min.png")

plt.figure()
sns.lineplot(x='t', y='max', hue='solver', data=freeSurf_min_max)
plt.savefig("results/freeSurf_max.png")


maxU = pd.read_csv("results/maxU.csv")

plt.figure()
sns.lineplot(x='t', y='U_x', hue='solver', data=maxU)
plt.savefig("results/U_x.png")

plt.figure()
sns.lineplot(x='t', y='U_y', hue='solver', data=maxU)
plt.savefig("results/U_y.png")

plt.figure()
sns.lineplot(x='t', y='U_z', hue='solver', data=maxU)
plt.savefig("results/U_z.png")

plt.figure()
sns.lineplot(x='t', y='dt', hue='solver', data=maxU)
plt.savefig("results/dt.png")


plt.show()
