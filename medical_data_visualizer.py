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
    df_heat = \
        df[(df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(df_heat.corr(), dtype=bool))



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(data=corr, 
                annot=True, 
                fmt=".1f", 
                linewidth=.5, 
                mask=mask, 
                annot_kws={'fontsize':6}, 
                cbar_kws={"shrink": .7}, 
                square=False, 
                center=0, 
                vmax=0.30);
  
  # 16
    fig.savefig('heatmap.png')
    return fig


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
