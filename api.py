import requests
import pandas as pd
import time
import sys

API_KEY = "579b464db66ec23bdd0000010cebaf31b6854cb77de768e7e2d13018"

def simulate_progress():
    for i in range(101):
        sys.stdout.write(f"\rFetching data... {i}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def fetch_aqi_data():
    url = f"https://api.data.gov.in/resource/3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69?api-key={API_KEY}&format=json&limit=100"
    print("Initiating AQI data fetch from data.gov.in...")
    simulate_progress()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['records']
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch AQI data: {response.status_code}")

def fetch_temperature_data():
    url = f"https://api.data.gov.in/resource/4c424514-cb21-4c21-9e17-17c0c156cc46?api-key={API_KEY}&format=json&limit=100"
    print("Initiating Temperature data fetch from data.gov.in...")
    simulate_progress()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['records']
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch Temperature data: {response.status_code}")

def fetch_rainfall_data():
    url = f"https://api.data.gov.in/resource/0e7a66c6-2a7f-4a78-9f9f-7e3e6d7e7e5e?api-key={API_KEY}&format=json&limit=100"
    print("Initiating Rainfall data fetch from data.gov.in...")
    simulate_progress()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['records']
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch Rainfall data: {response.status_code}")

def fetch_water_data():
    url = f"https://api.data.gov.in/resource/7c3b8f8e-4e4f-4b1f-8e2e-8c3b7e4e4e9f?api-key={API_KEY}&format=json&limit=100"
    print("Initiating Water Resource data fetch from data.gov.in...")
    simulate_progress()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['records']
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch Water Resource data: {response.status_code}")

def fetch_crop_yield_data():
    url = f"https://api.data.gov.in/resource/3d5e7b8e-1a2f-4c3f-8e1e-7c3b7e4e4e8f?api-key={API_KEY}&format=json&limit=100"
    print("Initiating Crop Yield data fetch from data.gov.in...")
    simulate_progress()
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['records']
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch Crop Yield data: {response.status_code}")