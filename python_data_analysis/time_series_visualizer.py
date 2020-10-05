import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', sep=',', header=0)
df.reset_index(inplace=True, drop=True)

# Clean data
df = df[(df.value <= df.value.quantile(0.975)) & (df.value >= df.value.quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,10))

    ax.plot(df.date, df.value, color='red')
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar2 = df_bar.groupby([df_bar.date.dt.year, df_bar.date.dt.month]).mean().round()
    df_bar2.index.names = ['year', 'month']
    df_bar2.reset_index(inplace=True)
    df_bar2.month = df_bar2.month.apply(lambda x: calendar.month_name[x])

    # df_bar2.head()

    # Draw bar plot
    # Bar Chart - Draw
    fig, ax = plt.subplots()
    g = sns.catplot(data=df_bar2, kind='bar', x='year', y='value', hue='month', palette='bright', legend_out=False)
    g.set_axis_labels('Years', 'Average Page Views')
    g.set_xticklabels(rotation=90)

    # Handle the Legend
    leg = g.axes.flat[0].get_legend()
    leg.set_title('Months')
    new_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for t, l in zip(leg.texts, new_labels): t.set_text(l)

    fig = g.fig


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2)
    ax1 = sns.boxplot(data=df_box, x='year', y='value', ax=ax[0])
    ax2 = sns.boxplot(data=df_box, x='month', y='value', order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=ax[1])

    ax1.set(xlabel='Year', ylabel='Page Views')
    ax1.set(title='Year-wise Box Plot (Trend)')

    ax2.set(xlabel='Month', ylabel='Page Views')
    ax2.set(title='Month-wise Box Plot (Seasonality)')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
