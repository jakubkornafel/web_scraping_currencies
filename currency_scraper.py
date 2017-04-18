# You will need to install "pandas" package in your virtual environment by using: pip install pandas


import pandas as pd

source = pd.read_html('https://cinkciarz.pl/kantor/kursy-walut-cinkciarz-pl')
x = (tr for tr in source)
for i in x:
    print(i)
