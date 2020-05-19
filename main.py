import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FastICA

from utils import read_data

metrics, pmd = read_data()

X1 = metrics.iloc[:, 10:].to_numpy()    # Keep only metric values
X2 = pmd.iloc[:, 10:].to_numpy()        # Keep only PMD values

# Treat missing values
X1 = SimpleImputer().fit_transform(X1)
X2 = SimpleImputer().fit_transform(X2)

# Scale data
metrics_scaler = StandardScaler()
pmd_scaler = StandardScaler()
X1 = metrics_scaler.fit_transform(X1)
X2 = pmd_scaler.fit_transform(X2)

# ICA
transformer = FastICA(n_components=2, random_state=0)

X1 = transformer.fit_transform(X1)
X2 = transformer.fit_transform(X2)

X1 = pd.DataFrame(data=X1, columns=['IC1', 'IC2'])
X2 = pd.DataFrame(data=X2, columns=['IC1', 'IC2'])

# Plot data with reduced dimensions
X1.plot.scatter('IC1', 'IC2')
X2.plot.scatter('IC1', 'IC2')

#------------------------------- Metrics -------------------------------------#
# Sample in the 2 high density areas of the metrics' lower dimentional space
area1 = (X1.IC1 > -0.005) & (X1.IC1 < 0.015) & (X1.IC2 > 0.005) & (X1.IC2 < 0.015)
area2 = (X1.IC1 > -0.005) & (X1.IC1 < 0.015) & (X1.IC2 < -0.005) & (X1.IC2 > -0.01)

m1 = metrics.loc[area1, :].iloc[:1000, 10:]
m2 = metrics.loc[area2, :].iloc[:1000, 10:]

m1 = pd.DataFrame(data = metrics_scaler.transform(m1), columns = m1.columns)
m2 = pd.DataFrame(data = metrics_scaler.transform(m2), columns = m2.columns)

useful_metrics = ['McCC', 'NL', 'NOI', 'CD', 'DLOC', 'MI', 'LOC', 'TLOC', 'CLLC']

m1 = m1.loc[:, useful_metrics]
m2 = m2.loc[:, useful_metrics]

plt.figure()
plt.title('Comparison of metrics values on the different areas')
m1.mean().plot()
m2.mean().plot()
plt.legend(['Area 1', 'Area 2'])

#--------------------------------- PMDs --------------------------------------#
# Sample in the 2 high density areas of the pmds' lower dimentional space
area1 = X2.IC1 > -0.03
area2 = X2.IC1 < -0.06

p1 = pmd.loc[area1, :].iloc[:1000, 10:]
p2 = pmd.loc[area2, :].iloc[:1000, 10:]

p1 = pd.DataFrame(data = pmd_scaler.transform(p1), columns = p1.columns)
p2 = pd.DataFrame(data = pmd_scaler.transform(p2), columns = p2.columns)

plt.figure()
plt.title('Comparison of PMD values on the different areas')
p1.mean().plot()
p2.mean().plot()
plt.legend(['Area 1', 'Area 2'])
