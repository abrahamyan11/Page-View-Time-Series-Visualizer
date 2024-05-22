import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    df_clean = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_clean.index, df_clean['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    plt.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_grouped.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.legend(title='Months')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.xticks(rotation=45)
    plt.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df, ax=axes[1], 
                order=['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December'])
    
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return fig
