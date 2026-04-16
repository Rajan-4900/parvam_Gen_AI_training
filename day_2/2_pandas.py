# pandas - python data analysis library
# 1. Series - 1D labeled array
# 2. DataFrame - 2D labeled data structure

import pandas as pd
# Series
s1 = pd.Series(["A", "B", "C", "D"], index=["a", "b", "c", "d"])
print(s1)

# data frame
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)