#import des librairies utiles
import pandas as pd

#importer le dataframe des datas du SNP
df = pd.read_csv("FTS_SNP.csv")

# afficher infos sur le dataframe importé
#print(df.shape)
#print(df.head())

# retirer les colonnes inutiles du dataframe
df = df.drop(columns = ["Open","High","Low"])
print(df.head())

df

