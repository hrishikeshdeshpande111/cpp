import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = '/Users/hrishikesh/Downloads/CPP- Hrishikesh - Diseases.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Clean the data
data['Geographical Spread'] = data['Geographical Spread'].str.replace(r'\d+', '')  # Remove footnotes from regions
data['Potential Market Size (USD Million)'] = pd.to_numeric(data['Potential Market Size (USD Million)'], errors='coerce')

# Bar chart: Top diseases by market size
fig1 = px.bar(
    data.sort_values('Potential Market Size (USD Million)', ascending=False).dropna(),
    x='Disease Name',
    y='Potential Market Size (USD Million)',
    title='Top Diseases by Potential Market Size',
    labels={'Potential Market Size (USD Million)': 'Market Size (USD Million)'},
    template='plotly_dark'
)
fig1.show()

# Pie chart: Research status distribution
fig2 = px.pie(
    data,
    names='Bacteriophage Research Status',
    title='Bacteriophage Research Status Distribution',
    template='plotly_dark'
)
fig2.show()

# Extract geographical spread and map it to the world regions
geographical_data = data[['Disease Name', 'Geographical Spread']].dropna()
geographical_data['Geographical Spread'] = geographical_data['Geographical Spread'].str.split(',')

# Generate the interactive world map with hover information
map_data = []
for index, row in geographical_data.iterrows():
    for region in row['Geographical Spread']:
        region = region.strip()
        map_data.append({'Disease Name': row['Disease Name'], 'Region': region})

geo_df = pd.DataFrame(map_data)

# World map visualization
fig3 = px.scatter_geo(
    geo_df,
    locations='Region',
    locationmode='country names',
    hover_name='Disease Name',
    title='Global Spread of Diseases',
    template='plotly_dark'
)
fig3.show()
