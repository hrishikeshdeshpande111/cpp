import plotly.express as px
import pandas as pd

# Data for the map
data = pd.DataFrame({
    "Country": ["United States", "India", "China", "Brazil", "Poland"],
    "Percentage": ["~35%", "~10–15%", "~20%", "~8–10%", "~15%"],
    "Highlight": ["High", "High", "High", "High", "High"],
})

# Plot the map
fig = px.choropleth(
    data,
    locations="Country",
    locationmode="country names",
    color="Highlight",
    title="High Poultry-Producing Countries and Their Market Share",
    color_discrete_map={"High": "skyblue"},
)

fig.update_layout(
    geo=dict(showframe=False, showcoastlines=False),
    title_x=0.5,
)
fig.show()


import plotly.figure_factory as ff

# Data for heatmap
regions = ["United States", "India", "China", "European Union (Poland)", "Brazil"]
prevalence = [80, 70, 85, 60, 75]  # Example prevalence scores
heatmap_data = [prevalence]
x_labels = regions

# Create the heatmap
fig = ff.create_annotated_heatmap(
    z=heatmap_data,
    x=x_labels,
    y=["Prevalence"],
    colorscale="Reds",
    annotation_text=[[f"{p}" for p in prevalence]],
)

fig.update_layout(title="Poultry Disease Prevalence by Region", title_x=0.5)
fig.show()


import plotly.graph_objects as go

# Data for pie chart
diseases = ["Colibacillosis (APEC)", "Necrotic Enteritis", "Salmonellosis", "Airborne APEC", "Campylobacteriosis"]
economic_impacts = [35, 15, 20, 15, 10]  # Based on percentage market shares

# Create pie chart
fig = go.Figure(
    data=[go.Pie(labels=diseases, values=economic_impacts, hole=0.3)]
)
fig.update_layout(title="Economic Impacts of Poultry Diseases", title_x=0.5)
fig.show()


import plotly.express as px

# Data for bar chart
data = pd.DataFrame({
    "Region": ["United States", "India", "China", "European Union (Poland)", "Brazil"],
    "Bacteriophage Therapy": [30, 40, 35, 25, 38],
    "Antibiotics": [50, 55, 60, 45, 52],
})

# Melt the data for grouped bar chart
data_melted = data.melt(id_vars="Region", var_name="Treatment", value_name="Cost")

# Plot the bar chart
fig = px.bar(
    data_melted,
    x="Region",
    y="Cost",
    color="Treatment",
    barmode="group",
    title="Comparative Cost-Effectiveness: Bacteriophage Therapy vs. Antibiotics",
    color_discrete_map={"Bacteriophage Therapy": "skyblue", "Antibiotics": "salmon"},
)

fig.update_layout(title_x=0.5, xaxis_tickangle=45)
fig.show()
