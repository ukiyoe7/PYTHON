## GEMINI PROJECT
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import google.generativeai as genai

# Define the scope and credentials for accessing Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(r"C:\Users\REPRO SANDRO\Documents\PYTHON\client_secret.json", scope)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Open the spreadsheet by its title
spreadsheet = client.open('TEST SHEET')

# Select a specific worksheet by its index (starting from 0) or title
worksheet = spreadsheet.get_worksheet(0)  # Use index (0 for the first worksheet)

# Get all values from the worksheet
all_values = worksheet.get_all_values()

# Join all values into a single string for Gemini analysis
data_for_analysis = '\n'.join(['\t'.join(row) for row in all_values])

# Define the question for Gemini
question = "read PDPDESCRICAO and check how many COMFORT there are?"

# Configure Gemini API
genai.configure(api_key="AIzaSyAKmuc5YClNDyJ5lU-hv9h8TgHpaBeeuGQ")

# Initialize the GenerativeModel
model = genai.GenerativeModel(model_name='gemini-1.0-pro')

# Start a chat session
chat = model.start_chat(enable_automatic_function_calling=True)

# Send data and question for analysis to Gemini
response = chat.send_message(data_for_analysis + "\n" + question)

# Try to access generations first (assuming format might change)
try:
    answer = response.generations[0].text
    print(answer)
except AttributeError:
    # Fallback to response.text if generations not available
    print(response.text)

    ## THIS CODE IS GREATE