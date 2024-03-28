import pandas as pd
# URL of the webpage containing the HTML table
url = 'https://en.wikipedia.org/wiki/National_Basketball_Association'

#nRead HTML tables from the webpage
tables = pd.read_html(url)

# If there are multiple tables on the webpage, you can select the desired one
# For example, select the first table
first_table_df = tables[0]

# Display the DataFrame representing the first table
print(first_table_df)