import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv', sep=',', header=0)

# Add 'overweight' column
def isOverweight(weight, height):
    if (weight / ((height/100) ** 2)) > 25:
        return 1
    else:
        return 0

df['overweight'] = df.apply(lambda row: isOverweight(row['weight'],row['height']), axis=1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize(value):
    if value == 1:
        return 0
    else:
        return 1

df['cholesterol'] = df.apply(lambda row: normalize(row['cholesterol']), axis=1)
df['gluc'] = df.apply(lambda row: normalize(row['gluc']), axis=1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars="cardio",value_vars=['cholesterol','gluc','smoke','alco','active','overweight']).sort_values(by="variable", ascending=True)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x="variable", col="cardio", data=df_cat, kind="count", hue="value")
    g.set_axis_labels("variable","total")
    fig = g.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df.ap_lo <= df.ap_hi) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    df_heat.info()

    # Calculate the correlation matrix
    corr = corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(15,10))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, center=0, vmax=0.32, vmin=-0.16, cbar_kws={"shrink": 0.5}, fmt='.1f', linewidths=0.5, annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
