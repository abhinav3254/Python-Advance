# import pandas

# mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

# # dataframe is 2d array with columns of potentially different types
# myvar = pandas.DataFrame(mydataset)

# print(myvar)

# reading csv files

import pandas as pd

# note this --> point If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# df = pd.read_csv(
#     "/Users/abhinavkumar/Desktop/datasets/archive/zudio/Men/Men/ACCESSORIES.csv"
# )
# print(df.to_string)


# reading json
df = pd.read_json("/Users/abhinavkumar/Desktop/datasets/amazon.books.json", lines=True)
print(df.to_string)
