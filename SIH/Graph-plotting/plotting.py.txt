import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1: Sort the DataFrame by the '2018' column to get the top 10 states with the most cyber crimes in 2018
top_10_states = df.sort_values(by='2018', ascending=False).head(10)

# Step 2: Seaborn Bar Plot
plt.figure(figsize=(12, 6))
sns.barplot(x='State/UT', y='2018', data=top_10_states, palette='viridis')
plt.title('Top 10 States by Cyber Crimes in 2018', fontsize=16)
plt.xticks(rotation=45)
plt.xlabel('State/UT', fontsize=12)
plt.ylabel('Number of Cyber Crimes (2018)', fontsize=12)
plt.show()

# Step 3: Plotly Bar Plot (Interactive) with Matching Layout
fig = px.bar(
    top_10_states,
    x='State/UT',
    y='2018',
    title='Top 10 States by Cyber Crimes in 2018',
    labels={'State/UT': 'State/UT', '2018': 'Cyber Crimes in 2018'},
    text='2018'
)

# Adjusting layout to match the Seaborn chart's size and look
fig.update_layout(
    width=900,  # Adjust width to match the Seaborn figure
    height=600,  # Adjust height to match the Seaborn figure
    title_font_size=16,  # Title font size
    xaxis_title='State/UT',  # X-axis title
    yaxis_title='Number of Cyber Crimes (2018)',  # Y-axis title
    xaxis_tickangle=-45,  # Rotate the x-axis labels to match Seaborn's rotation
    font=dict(
        size=12  # General font size to match Seaborn's font size
    )
)

# Show the interactive Plotly chart
fig.show()
