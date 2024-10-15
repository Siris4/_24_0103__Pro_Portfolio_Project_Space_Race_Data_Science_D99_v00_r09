import pandas as pd
import plotly.express as px

# Load the CSV data into a DataFrame
csv_file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0103__Day99_Pro_Portfolio_Project_Space_Race_Data_Science_241014\NewProject\r00_env_START\r08\space_launches.csv'
df = pd.read_csv(csv_file_path)

# Define a mapping of launch pad locations to countries (as in previous code)
launchpad_to_country = {
    "Kennedy Space Center": "USA",
    "Cape Canaveral": "USA",
    "Vandenberg": "USA",
    "Starbase": "USA",
    "Baikonur Cosmodrome": "Kazakhstan",
    "Plesetsk Cosmodrome": "Russia",
    "Xichang Satellite Launch Center": "China",
    "Jiuquan Satellite Launch Center": "China",
    "Tanegashima Space Center": "Japan",
    "Guiana Space Centre": "French Guiana",
    "Māhia Peninsula": "New Zealand"
}

# Extract the country from the 'Launch Pad' column using the mapping
df['Country'] = df['Launch Pad'].apply(lambda x: next((country for pad, country in launchpad_to_country.items() if pad in x), 'Unknown'))

# Create a sunburst chart hierarchy: Country -> Company -> Mission
fig = px.sunburst(df,
                  path=['Country', 'Company', 'Mission'],  # Define the hierarchy
                  title="Space Launches by Country, Company, and Mission")

# Show the sunburst chart
fig.show()
