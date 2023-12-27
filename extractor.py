import re
import datetime
import pandas as pd

term = 'hash:'
file = 'hashes.txt'

PATTERN = fr'(\b{term}\b[a-zA-Z]+|\b{term}\s\b[a-zA-Z]+)'
data_txt=''
with open(file,"r", encoding="utf8") as f:
    data_txt = f.readlines()
whole_txt = "".join(data_txt)
matches = re.findall(PATTERN,whole_txt,flags=re.MULTILINE)
expenses = [m.split(",")[0].split(term)[1].strip() for m in matches]
df = pd.DataFrame(data=expenses)
df.reset_index(inplace=True)
df.columns = ["ID","RESULTS"]
df = df.drop('ID', axis=1)
df.to_csv("result.txt", index=False)
