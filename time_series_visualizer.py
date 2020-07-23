import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import sys

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv')
print(df)

df.set_index('date', drop=True, inplace=True)
df.index=[pd.Timestamp(dt) for dt in df.index]
# print(df.index)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
print(df)

def draw_line_plot():
  # Draw line plot
  fig, axis = plt.subplots(1,1)
  
  fig.set_figwidth(15)
  fig.set_figheight(5)

  plt.plot(df.index, df['value'], color='r')

  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  plt.xlabel('Date')
  plt.ylabel('Page Views')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()

  # Draw bar plot
  month_label = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  year_label = [2016, 2017, 2018, 2019]
  months = np.zeros([len(month_label), len(year_label)])

  for i in range(len(month_label)):
      for j, year in enumerate(year_label):
          t = df[df.index.year == year]
          months[i][j] = t[t.index.month == i].value.mean()

  x = np.arange(len(year_label))
  fig, ax = plt.subplots()
  fig.set_figwidth(12)
  fig.set_figheight(10)
  for i, month in enumerate(months):
      ax.bar(x - (0.5 * (len(month_label) - i) / len(month_label)), months[i], 0.5/len(month_label), label=month_label[i], fontsize='14')

  plt.xticks(rotation=90, horizontalalignment="center")
  ax.set_ylabel("Average Page Views", fontsize='14')
  ax.set_xlabel("Years", fontsize='14')
  ax.set_xticks(x)
  ax.set_xticklabels(year_label, fontsize='14')
  ax.legend(title='Months', loc=2, fontsize='14')
  
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  sys.exit()
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)





  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
