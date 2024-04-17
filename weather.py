import requests
import pandas as pd
    

def get_forecast(api_key, lat, lon, city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'  # Adjusted URL for 7-day forecast
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extract forecast information
            forecast_days = data['list']
            forecast_data = []
            
            for day in forecast_days:
                date = day['dt_txt']
                max_temp_c = day['main']['temp_max']
                min_temp_c = day['main']['temp_min']
                avg_temp_c = day['main']['temp']
                condition = day['weather'][0]['description']
                
                # Simulating solar irradiation value
                solar_irradiation = 5.8  # This value should be obtained from a suitable source
                
                forecast_data.append({
                    'City': city,
                    'Latitude': lat,
                    'Longitude': lon,
                    'Date': date,
                    'Max Temperature (C)': max_temp_c,
                    'Min Temperature (C)': min_temp_c,
                    'Avg Temperature (C)': avg_temp_c,
                    'Condition': condition,
                    'Solar Irradiation': solar_irradiation
                })
            
            # Create a DataFrame
            df = pd.DataFrame(forecast_data)
            
            return df
        else:
            print(f"Error: {data['message']}")
            return None
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Replace 'YOUR_API_KEY' with your actual WeatherAPI key
api_key = '9b20c9532ef3018ebfa7149971ac17e6'
locations = [
    {'city': 'Florianopolis', 'lat': -27.593500, 'lon': -48.558540},
    {'city': 'Sao Paulo', 'lat': -23.5505, 'lon': -46.6333},
    {'city': 'Porto Alegre', 'lat': -30.0346, 'lon': -51.2177}
]

# Get forecast data for multiple cities and concatenate into a single DataFrame
forecast_dfs = []
for location in locations:
    df = get_forecast(api_key, location['lat'], location['lon'], location['city'])
    if df is not None:
        forecast_dfs.append(df)

# Concatenate forecast DataFrames
final_forecast_df = pd.concat(forecast_dfs, ignore_index=True)

# Export DataFrame to CSV file
final_forecast_df.to_csv('C:/Users/REPRO SANDRO/Documents/PYTHON/WEATHER/forecast_data.csv', index=False)
