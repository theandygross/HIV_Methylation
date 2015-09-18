#!/cellar/users/agross/anaconda2/bin/python

import sys
import pandas as pd
import statsmodels.api as sm

store = sys.argv[1]
outdir = sys.argv[2]
table_name = sys.argv[3]
out_suffix = sys.argv[4]
covariates = sys.argv[5:]
print sys.argv

c_age = pd.read_hdf(store, 'age')
hiv = pd.read_hdf(store, 'HIV')
cell_counts = pd.read_hdf(store, 'cell_counts')
df = pd.read_hdf(store, table_name)

intercept = pd.Series(1, index=hiv.index)

X = pd.concat([intercept, hiv, cell_counts.CD4T, cell_counts.CD8T,
               cell_counts.NK, cell_counts.Bcell, cell_counts.Mono,
               c_age], axis=1, 
              keys=['Intercept','HIV', 'CD4T','CD8T','NK','Bcell','Mono',
                    'age'])
X = X.ix[df.columns]
X = X.dropna()
X = X[['HIV','Intercept'] + covariates]

X_reduced = X[['Intercept'] + covariates]
print X.shape

p = {}
d_hiv = {}
w = (len(hiv) - hiv.map(hiv.value_counts())).astype(float) / len(hiv)
w = w.ix[X.index]
df = df.ix[:, X.index]

for i,y in df.iterrows():
    y.name = 'marker'
    mod_all = sm.WLS(y, X, weights=w)
    res_ref = mod_all.fit()
    p[i] = res_ref.params
    
    mod_reduced = sm.WLS(y, X_reduced, weights=w)
    m1 = mod_reduced.fit()
    d_hiv[i] = res_ref.compare_lr_test(m1)

p = pd.DataFrame(p).T
d_hiv = pd.DataFrame(d_hiv, index=['LR','p','df']).T

out = pd.concat([p, d_hiv], 
                keys=['multi_variate','HIV_LR'],
                axis=1)
out.to_csv('{}/{}_{}.csv'.format(outdir, table_name, out_suffix))