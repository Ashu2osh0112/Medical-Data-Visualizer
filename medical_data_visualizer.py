import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medacl_examination.csv')

# 2
def bmi(df):
  if (df['weight'] / ((df['height']/100)**2)) > 25:
    return 1
  else:
    return 0

df['overweight'] = df.apply(bmi, axis =1)


# 3
def normalize(df):
  if df['gluc'] == 1 or df['cholesterol'] == 1:
    return 0
  else:
    return 1
df['gluc'] = df.apply(normalize, axis = 1)
df['cholesterol'] = df.apply(normalize, axis = 1)


# 4
def draw_cat_plot():
     # 5
    df_cat = df.melt(id_vars = 'cardio', 
                     value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], 
                     value_name='value')
    # 6


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    catplot = sns.catplot(data=df_cat, x = 'variable', y = 'total', 
                          col = 'cardio', kind = 'bar', hue = 'value')


    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
