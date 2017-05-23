import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, confusion_matrix, classification_report
from scipy.optimize import minimize

#label = pd.read_csv("data/label.csv")
#print label.shape[1] 

train = pd.read_csv("train.tsv", sep="\t")
test = pd.read_csv("test.tsv", sep="\t")

train.drop("tag", axis=1, inplace=True)

full = pd.concat([train, test], axis=0).reset_index(drop=True)

seller_cnt = full["Seller"].value_counts()
print seller_cnt
selected_seller = seller_cnt[seller_cnt > 100].index.tolist()
print selected_seller

full.loc[~full["Seller"].isin(selected_seller), "Seller"] = ""
full.loc[:, "Seller"] = LabelEncoder().fit_transform(full["Seller"])
print full["Seller"]

#print ~full["Actors"].isnull() * 1
full.loc[:, "Actors"] = ~full["Actors"].isnull() * 1
print full["Actors"]