import pandas as pd

source = pd.read_html('https://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl')
x = (tr for tr in source)
for i in x:
    print(i)
