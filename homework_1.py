import pandas as pd
import random
import numpy as np
from sklearn.preprocessing import LabelEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

le = LabelEncoder()
labels = le.fit_transform(lst)
oh_labels = np.eye(2)[labels]

data = pd.DataFrame({'whoAmI': lst})
data_one_hot = pd.DataFrame(oh_labels, columns=['whoAmI_0', 'whoAmI_1'])
print(data_one_hot.head())
