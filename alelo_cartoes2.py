import requests
import pandas as pd

# Define your login credentials
username = 'your_username'
password = 'your_password'

# URL for the login page
login_url = 'https://prepagos.alelo.com.br/auth/login'

# Create a session
session = requests.Session()

# Perform login
payload = {
    'handle': username,
    'password': password
}
response = session.post(login_url, data=payload)

# Check if login was successful (you can add more validation here)
if 'Welcome' in response.text:
    print("Login successful!")
else:
    print("Login failed. Check your credentials.")

# Navigate to the "Incentivo" menu
incentivo_url = 'https://prepagos.alelo.com.br/cartoes'
response = session.get(incentivo_url)

# Perform a search (you'll need to inspect the page to find the relevant form fields)
# Example: fill in form fields and submit the search
# ...

# Extract data (you'll need to identify the table or element containing the data)
# Example: use pandas to read the HTML content and extract the relevant table
df_list = pd.read_html(response.content)
df = df_list[-1]  # Assuming the last table contains the data

# Export data to a CSV file
output_file = 'my_data.csv'
df.to_csv(output_file, index=False)
print(f"Data exported to {output_file}")
