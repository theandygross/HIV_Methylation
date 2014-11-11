#!/cellar/users/agross/anaconda2/bin/python

import sys

import pandas as pd
import statsmodels.api as sm

store = sys.argv[1]
outdir = sys.argv[2]
table_name = sys.argv[3]

fmla = 'marker ~ age + CD4T + CD8T + NK + Bcell + Mono + study'

c_age = pd.read_hdf(store, 'age')
b_age = pd.read_hdf(store, 'bio_age')
gender = pd.read_hdf(store, 'gender')
age_adv = b_age - c_age
age = c_age

cell_counts = pd.read_hdf(store, 'cell_counts')
df = pd.read_hdf(store, table_name)
df = df.dropna(1)

intercept = pd.Series(1, index=df.columns)
X = pd.concat([intercept, age, cell_counts.CD4T, cell_counts.CD8T,
               cell_counts.NK, cell_counts.Bcell, cell_counts.Mono,
               gender, age_adv], axis=1, 
              keys=['Intercept','age', 'CD4T','CD8T','NK','Bcell','Mono',
                    'gender', 'age_adv'])
X = X.dropna()
idx = X.index.intersection(df.columns)
X = X.ix[idx]
df = df.ix[:, idx]

X_HIV = X[['Intercept','CD4T','CD8T','NK','Bcell','Mono','gender', 'age']]

p = {}
d_hiv = {}
#w = (len(hiv) - hiv.map(hiv.value_counts())).astype(float) / len(hiv)
#w = w.ix[X.index]

for i,y in df.iterrows():
    y.name = 'marker'
    #mod_all = sm.WLS(y, X, weights=w)
    mod_all = sm.OLS(y, X)
    res_ref = mod_all.fit()
    p[i] = res_ref.params
    
    #mod_hiv = sm.WLS(y, X_HIV, weights=w)
    mod_hiv = sm.OLS(y, X_HIV)
    m1 = mod_hiv.fit()
    d_hiv[i] = res_ref.compare_lr_test(m1)

p = pd.DataFrame(p).T
d_hiv = pd.DataFrame(d_hiv, index=['LR','p','df']).T

out = pd.concat([p, d_hiv], 
                keys=['multi_variate','age_adv_LR'],
                axis=1)
out.to_csv('{}/{}_age_adv_out.csv'.format(outdir, table_name))