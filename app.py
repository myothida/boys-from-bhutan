#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dash import Dash, dash_table
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

import pandas as pd
import random


# In[2]:


df=pd.read_csv('grade10.csv')
df1=pd.read_csv('grade12.csv')


# In[3]:


def getkiran():
    df10 = df[df['Name']=="Kiran"]
    df10 = df[df['Name']=="Kiran"]
    df12 = df1[df1['Name']=="Kiran"]
    dfk = pd.concat([df10, df12])
    return dfk


# In[4]:


def getnamgay():
    df10 = df[df['Name']=="Namgay"]
    df10 = df[df['Name']=="Namgay"]
    df12 = df1[df1['Name']=="Namgay"]
    dfn = pd.concat([df10, df12])
    return dfn


# In[5]:


app = JupyterDash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# In[6]:


app.layout = dbc.Container([
    
    html.Div([
        dbc.Tabs([
            dbc.Tab(label="Kiran", tab_id="kiran"),
            dbc.Tab(label="Namgay", tab_id="NT"),
            dbc.Tab(label="Grade 10", tab_id="G10"),
            dbc.Tab(label="Grade 12", tab_id="G12"),
            
        ],id="tabs",active_tab="Kiran"),
    ]),
        
    html.Div(id="table")
    
    
])


# In[7]:


@app.callback(
    Output("table", "children"),
    Input('tabs','active_tab'),
)

def make_table(atab):
    if (atab =='kiran'):
        df = getkiran()
        
    elif(atab == 'NT'):
        df = getnamgay()
        
    elif(atab == 'G10'):
        df = df=pd.read_csv('grade10.csv')
        
    elif(atab == 'G12'):
        df = df=pd.read_csv('grade12.csv')

        
    else:
        df=pd.read_csv('grade12.csv')
        
    return dbc.Table.from_dataframe(df, striped=True, bordered=True, color = "primary", hover=True)


# In[8]:


if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)    
    url = "http://127.0.0.1:{0}".format(port)    
    app.run_server(use_reloader=False, debug=True, port=port)


# In[ ]:




