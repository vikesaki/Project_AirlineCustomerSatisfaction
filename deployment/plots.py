import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('deployment/train.csv', index_col=0)

discrete_columns = [
    'Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking',
    'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
    'Inflight entertainment', 'On-board service', 'Leg room service',
    'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness'
]

combined = train.copy(deep=True)
combined['Total Delay'] = combined['Departure Delay in Minutes'].fillna(0) + combined['Arrival Delay in Minutes'].fillna(0)
distance_bins = [0, 500, 1000, 1500, 2000, combined['Flight Distance'].max()]
distance_labels = ['0–500', '501–1000', '1001–1500', '1501–2000', '2000+']
combined['FlightRange'] = pd.cut(combined['Flight Distance'], bins=distance_bins, labels=distance_labels)

def correlation_matrix(df, variables=None, method='pearson', cmap="coolwarm", target=None, annotation="horizontal"):
    try:
        if variables is None:
            variables = list(df.select_dtypes(include='number'))
        matrix = df[variables].corr(method=method)

        if target:
            matrix = matrix[[target]].T

        rotation = 0 if annotation == 'horizontal' else 90
        
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_alpha(0)
        sns.heatmap(matrix, annot=True, cmap=cmap, fmt=".3f", annot_kws={"rotation": rotation}, ax=ax)
        ax.set_title("Correlation Matrix")
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')

        ax.set_facecolor('none') 
        return fig

    except Exception as e:
        print(f'Error occurred: {e}')
        return None

def satisfaction_distribution():
    satisfaction_counts = train['satisfaction'].value_counts()
    fig, ax = plt.subplots(figsize=(6,6))
    fig.patch.set_alpha(0)
    result = ax.pie(
        satisfaction_counts,
        labels=train['satisfaction'].unique(),  # type: ignore
        autopct='%1.1f%%',
        colors=sns.color_palette('Set2')
    )
    wedges, texts = result[0], result[1]
    autotexts = result[2] if len(result) == 3 else []

    ax.set_title('Satisfaction Distribution')
    for text in texts:
        text.set_color('white')
    for autotext in autotexts:
        autotext.set_color('white')

    ax.set_facecolor('none') 
    ax.title.set_color('white')
    return fig

def satisfaction_gender():
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    sns.countplot(data=train, x='Gender', hue='satisfaction', palette='pastel', hue_order=['satisfied', 'neutral or dissatisfied'], ax=ax)
    ax.set_title('Satisfaction by Gender')

    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_facecolor('none') 
    return fig

def satisfaction_age():
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.patch.set_alpha(0)
    sns.histplot(data=train, x='Age', hue='satisfaction', multiple='fill', palette='muted', hue_order=['satisfied', 'neutral or dissatisfied'], ax=ax)
    ax.set_title('Age Distribution by Satisfaction')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_facecolor('none') 
    return fig

def satisfaction_class():
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    sns.countplot(data=train, x='Class', hue='satisfaction', palette='pastel', order=['Eco', 'Eco Plus', 'Business'], hue_order=['satisfied', 'neutral or dissatisfied'], ax=ax)
    ax.set_title('Satisfaction by Class')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_facecolor('none') 
    return fig

def delay_comparison():
    g = sns.lmplot(data=train, x='Departure Delay in Minutes', y='Arrival Delay in Minutes', line_kws={'color': 'red'})
    g.set(xlim=(0, 300), ylim=(0, 300))
    g.figure.patch.set_alpha(0)
    ax = g.ax
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    g.ax.title.set_color('white')

    ax.set_facecolor('none') 
    return g.figure

def flight_delay():
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_alpha(0)
    sns.boxplot(data=combined, x='FlightRange', y='Total Delay', hue='FlightRange', palette='Set2', ax=ax)
    ax.set_title('Total Delay Distribution by Flight Distance Range')
    ax.set_xlabel('Flight Distance Range (miles)')
    ax.set_ylabel('Total Delay (minutes)')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_facecolor('none') 
    fig.tight_layout()
    return fig

def satisfaction_checkin():
    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    sns.violinplot(
        data=train,
        x='Checkin service',
        y='satisfaction',
        hue='satisfaction',
        palette='Set3',
        split=True,
        ax=ax
    )
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')

    ax.set_facecolor('none') 
    ax.set_title('Check-in Service Rating by Satisfaction')
    return fig

def satisfaction_correlation():
    df_encoded = train.copy()
    df_encoded['satisfaction'] = df_encoded['satisfaction'].map({'satisfied': 1, 'neutral or dissatisfied': 0})
    selected_cols = discrete_columns + ['satisfaction']
    return correlation_matrix(df_encoded[selected_cols], target='satisfaction', annotation='vertical')
