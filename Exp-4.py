#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Married': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'Dependents': ['0', '1', '2', '3+', '0', '2', '1', '3+', '0', '1'],
    'Education': ['Graduate', 'Graduate', 'Not Graduate', 'Graduate', 'Graduate',
                  'Not Graduate', 'Graduate', 'Graduate', 'Not Graduate', 'Graduate'],
    'Self_Employed': ['No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No'],
    'Property_Area': ['Urban', 'Rural', 'Semiurban', 'Urban', 'Rural',
                      'Semiurban', 'Urban', 'Rural', 'Semiurban', 'Urban'],
    'ApplicantIncome': [5000, 3000, 7000, 4500, 3500, 6000, 4000, 5500, 8000, 3200],
    'CoapplicantIncome': [1500, 0, 2000, 1000, 500, 1500, 0, 1200, 2500, 800],
    'LoanAmount': [200, 120, 250, 180, 150, 220, 160, 210, 300, 140]
}

df = pd.DataFrame(data)

print("Dataset created successfully!")
print(df)


# In[2]:


print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataFrame Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)


# In[3]:


categorical_cols = [
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area'
]

for col in categorical_cols:
    unique_vals = df[col].unique()
    print(f"\nUnique values in '{col}': {unique_vals}")


# In[4]:


df['Dependents'] = df['Dependents'].replace('3+', 3)

df['Dependents'] = pd.to_numeric(
    df['Dependents'],
    errors='coerce'
).astype('Int64')

print("\nValue counts in 'Dependents' after conversion:")
print(df['Dependents'].value_counts(dropna=False))


# In[5]:


cols = [
    'ApplicantIncome',
    'CoapplicantIncome',
    'LoanAmount'
]

for col in cols:
    print(f"\nStatistics for '{col}':")
    
    print(f"Mean: {df[col].mean():.2f}")
    print(f"Median: {df[col].median():.2f}")
    print(f"Mode: {df[col].mode().values}")
    print(f"Range: {df[col].max() - df[col].min():.2f}")
    print(f"Variance: {df[col].var():.2f}")
    print(f"Standard Deviation: {df[col].std():.2f}")


# In[ ]:




