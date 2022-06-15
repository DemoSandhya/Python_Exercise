from xml.etree.ElementTree import tostringlist
from bs4 import BeautifulSoup
import json
import pandas as pd

from matplotlib import type1font
from nbformat import read

def Q1(X, Y):
    with open('test_payload1.xml', 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")
    Bs_data.DEPART.string = X
    Bs_data.RETURN.string = Y
    headTag = Bs_data.string

    with open("tsak1.xml", "wb") as writer:
        writer.write(Bs_data.encode())

def Q2(X):
    with open('test_payload.json', 'r') as f:
        data = json.load(f)
   
    # print(data)
    for i in data.keys():
        # print(data[i])

        if i == X:
            del data[i]
            break
        else:
            s = str(type(data[i]))
            # print(s)
            if s == "<class 'dict'>":
                for j in data[i].keys():
                    if j == X:
                        del data[i][j]
                        break
    
    with open('task2.json', 'w') as f:
        json.dump(data, f)

def Q3(inp):
    with open(inp, 'r') as f:
        data = f.readlines()
    cols = data[0].split(",")
    cols[-1] = cols[-1][0:-1]
    # print(cols)
    df = pd.DataFrame(columns=cols)
    for i in range(1,len(data)):
        newRow = data[i].split(",")    
        newRow[-1] = newRow[-1][0:-1]
        df.loc[len(df)] = newRow        
    df.to_csv(r'task3.csv', index=False)

# Q3('Jmeter_log1.jtl')