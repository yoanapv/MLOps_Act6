import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# TODO: Modify this list to include the numerical columns
NUMERICAL_VARS = ["pclass", "age", "sibsp", "parch", "fare"]]

# Crear custom transformer


class MissingIndicator(BaseEstimator, TransformerMixin):

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        # TODO: Put your code here
        for i in self.variables:
            X[i + "_nan"] = X[i].isna().map({True: 1, False: 0})
        return X


# Leer el csv sin aplicar transformaciones
df = pd.read_csv("raw-data.csv")

# Imprimir los primeros datos
print(df.head(50))

for i in NUMERICAL_VARS:
    print(i + "_nan", type(df[i]))

mi = MissingIndicator(variables=NUMERICAL_VARS)
# Aplicar las transformaciones
df_mi = mi.transform(df)

# Imprimir resultados despues de las transformaciones
print(df_mi.head(50))
