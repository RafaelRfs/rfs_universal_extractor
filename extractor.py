import re
import datetime
import pandas as pd

print('[+]Informe o padrao a ser encontrado, exemplo:  hash:')
term = input()

print('[+]Informe o nome do arquivo com os dados brutos, exemplo:  log.txt')
file = input()

print('[+]Informe o nome do arquivo que sera gerado os resultados,  exemplo:  result.txt')
result = input()

PATTERN = fr'(\b{term}\b[a-zA-Z0-9]+|\b{term}\s\b[a-zA-Z0-9]+)'

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

df.to_csv(result, index=False)
