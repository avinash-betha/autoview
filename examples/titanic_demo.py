import pandas as pd
from autoview import explore

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
explore(df, plots=True, target="Survived", show_missing=False)
# Only basic stats + missing data
#explore(df)

# Skip plots completely
#explore(df, plots=False, show_missing=False)