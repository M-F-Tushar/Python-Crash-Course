# Chapter 16: Downloading Data - Complete Study Guide

## Overview
This chapter teaches you how to download data sets from online sources and create working visualizations. You'll learn to work with two common data formats: CSV and JSON, and create meaningful visualizations using Matplotlib and Plotly.

## Learning Objectives
By the end of this chapter, you will:
- Process CSV files using Python's csv module
- Analyze weather data and create temperature charts
- Handle missing data with error checking
- Work with JSON format for geographical data
- Create interactive world maps showing earthquake data
- Understand date/time formatting and manipulation

---

## Part 1: Working with CSV Files

### What is CSV Format?

**CSV (Comma-Separated Values)** is a simple way to store data in text files where values are separated by commas.

**Example CSV format:**
```
"USW00025333","SITKA AIRPORT, AK US","2018-01-01","0.45",,"48","38"
```

**Key Characteristics:**
- Each line represents a data record
- Values are separated by commas
- Headers in the first row describe the data
- Easy for programs to process
- Can be tricky for humans to read

### Setting Up Your Project Structure

Create the following folder structure:
```
your_project_folder/
├── data/
│   ├── sitka_weather_07-2018_simple.csv
│   ├── sitka_weather_2018_simple.csv
│   └── death_valley_2018_simple.csv
└── your_python_files.py
```

### Parsing CSV File Headers

**Purpose:** Understanding what data is available in your CSV file

**Code Example:**
```python
import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```

**Output:**
```
['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
```

**Header Meanings:**
- **STATION**: Weather station code
- **NAME**: Weather station name
- **DATE**: Date of recording
- **PRCP**: Precipitation amount
- **TAVG**: Average temperature
- **TMAX**: Maximum temperature (high)
- **TMIN**: Minimum temperature (low)

### Finding Header Positions

**Why it matters:** You need to know which column contains which data

**Code Example:**
```python
import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

**Output:**
```
0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN
```

**Key Insight:** Date is at index 2, high temperature (TMAX) at index 5, low temperature (TMIN) at index 6.

### Extracting and Reading Data

**Goal:** Extract high temperatures from the CSV file

**Complete Code Example:**
```python
import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperatures from this file
    highs = []
    for row in reader:
        high = int(row[5])  # Convert string to integer
        highs.append(high)

print(highs)
```

**Output:**
```
[62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59, 64, 60, 60, 61, 65, 65, 63, 59, 64, 65, 68, 66, 64, 67, 65]
```

**Key Points:**
- `csv.reader()` automatically handles comma separation
- `next(reader)` skips the header row
- `int()` converts string data to numbers
- Data is stored in a list for later processing

### Creating Your First Temperature Chart

**Complete Code Example:**
```python
import csv
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperatures
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```

**Explanation:**
- `plt.style.use('seaborn')`: Makes the chart look more professional
- `fig, ax = plt.subplots()`: Creates figure and axis objects
- `ax.plot(highs, c='red')`: Plots data in red
- `plt.title()`, `plt.xlabel()`, `plt.ylabel()`: Add labels
- `plt.tick_params()`: Adjusts tick mark appearance

### Working with Dates - The datetime Module

**Problem:** Raw dates are strings; we need date objects for better plotting

**Understanding strptime():**
```python
from datetime import datetime

# Convert string to datetime object
first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)  # Output: 2018-07-01 00:00:00
```

**Date Format Codes (Table 16-1):**
| Code | Meaning | Example |
|------|---------|---------|
| %A | Weekday name | Monday |
| %B | Month name | January |
| %m | Month number | 01 to 12 |
| %d | Day of month | 01 to 31 |
| %Y | Four-digit year | 2019 |
| %y | Two-digit year | 19 |
| %H | Hour (24-hour) | 00 to 23 |
| %I | Hour (12-hour) | 01 to 12 |
| %p | AM or PM | am/pm |
| %M | Minutes | 00 to 59 |
| %S | Seconds | 00 to 61 |

### Plotting Dates on X-axis

**Complete Code Example:**
```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temperatures
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # Format dates diagonally
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```

**Key Addition:**
- `fig.autofmt_xdate()`: Automatically formats date labels to prevent overlap

### Plotting a Longer Timeframe

**Using Full Year Data:**
```python
# Change filename to use full year data
filename = 'data/sitka_weather_2018_simple.csv'
# Update title
plt.title("Daily high temperatures - 2018", fontsize=24)
```

This creates a chart showing temperature patterns across an entire year.

### Plotting Multiple Data Series

**Adding Low Temperatures:**
```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, high and low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])  # Low temperature at index 6
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot both high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')    # Highs in red
ax.plot(dates, lows, c='blue')    # Lows in blue

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```

### Shading Areas in Charts

**Adding Fill Between High and Low:**
```python
# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)     # Semi-transparent lines
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Rest of formatting code...
```

**Parameters Explained:**
- `alpha=0.5`: Makes lines semi-transparent
- `fill_between()`: Fills area between two data series
- `facecolor='blue'`: Color of filled area
- `alpha=0.1`: Very transparent fill

### Error Checking and Handling Missing Data

**The Problem:** Some weather stations have missing data that causes crashes

**Example Error:**
```
ValueError: invalid literal for int() with base 10: ''
```

**Solution - Using try-except-else:**
```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])  # Note: Different index for Death Valley
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the data
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```

**Error Handling Explanation:**
- `try`: Attempt to convert data to integers
- `except ValueError`: Handle missing data (empty strings)
- `else`: Only execute if no error occurred
- Missing data is skipped gracefully

### Downloading Your Own Weather Data

**Step-by-Step Process:**

1. **Visit NOAA Website:**
   - Go to https://www.ncdc.noaa.gov/cdo-web/
   - Click "Search Tool" in Discover Data By section
   - Choose "Daily Summaries"

2. **Select Location and Date:**
   - Choose date range
   - Select "ZIP Codes" in Search For section
   - Enter ZIP code and click Search

3. **Choose Station:**
   - Click "View Full Details" or click map then "Full Details"
   - Scroll down and click "Station List"
   - Choose a station and click "Add to Cart"

4. **Configure Download:**
   - Select "Custom GHCN-Daily CSV"
   - Verify date range
   - Click Continue

5. **Select Data Types:**
   - Choose specific data (temperature, precipitation, etc.)
   - Click Continue

6. **Complete Order:**
   - Enter email address
   - Click Submit Order
   - Wait for download link via email

---

## Exercises: Try It Yourself (16-1 to 16-5)

### Exercise 16-1: Sitka Rainfall
**Goal:** Visualize precipitation data from the PRCP column

**Solution Approach:**
```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, precipitations = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            precipitation = float(row[3])  # PRCP at index 3
        except ValueError:
            print(f"Missing precipitation data for {current_date}")
        else:
            dates.append(current_date)
            precipitations.append(precipitation)

# Create precipitation chart
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitations, c='blue')
plt.title("Daily Precipitation - Sitka, AK 2018", fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel("Precipitation (inches)", fontsize=12)
fig.autofmt_xdate()
plt.show()
```

### Exercise 16-2: Sitka–Death Valley Comparison
**Goal:** Create charts with identical y-axis scales for comparison

**Solution Approach:**
```python
# After creating both charts, set identical y-axis limits
plt.ylim(20, 120)  # Set same temperature range for both charts
```

### Exercise 16-3: San Francisco Weather
**Goal:** Download and analyze San Francisco weather data

**Process:**
1. Download San Francisco weather data using NOAA steps
2. Modify the code to use San Francisco data file
3. Create temperature visualization
4. Compare patterns with Sitka and Death Valley

### Exercise 16-4: Automatic Indexes
**Goal:** Use header row to find TMIN and TMAX positions automatically

**Solution Approach:**
```python
# Find indexes automatically
tmax_index = header_row.index('TMAX')
tmin_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

# Use these indexes in your loop
high = int(row[tmax_index])
low = int(row[tmin_index])
station_name = row[name_index]

# Generate title automatically
title = f"Temperatures for {station_name}"
```

### Exercise 16-5: Explore
**Goal:** Create additional visualizations exploring other weather aspects

**Ideas:**
- Average temperature trends
- Seasonal precipitation patterns
- Temperature ranges (difference between high and low)
- Comparison of multiple locations

---

## Part 2: Working with JSON Format

### What is JSON?

**JSON (JavaScript Object Notation)** is a format for storing data that uses key-value pairs.

**Characteristics:**
- More flexible than CSV
- Can store nested data structures
- Common for web APIs and geographical data
- Uses dictionaries and lists

### JSON Structure Example

**Raw JSON (hard to read):**
```json
{"type":"FeatureCollection","metadata":{"generated":1550361461000,...
```

**Formatted JSON (readable):**
```json
{
    "type": "FeatureCollection",
    "metadata": {
        "generated": 1550361461000,
        "title": "USGS Magnitude 1.0+ Earthquakes, Past Day",
        "count": 158
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 0.96,
                "title": "M 1.0 - 8km NE of Aguanga, CA"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-116.7941667, 33.4863333, 3.22]
            }
        }
    ]
}
```

### Exploring JSON Data Structure

**Code to Format JSON for Reading:**
```python
import json

# Load and reformat JSON for readability
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
```

**Key Functions:**
- `json.load(f)`: Loads JSON from file into Python data structure
- `json.dump(data, f, indent=4)`: Writes formatted JSON to file

### Understanding Earthquake Data Structure

**Key Components:**
1. **Metadata:** Information about the dataset
2. **Features:** List of individual earthquakes
3. **Properties:** Earthquake details (magnitude, title, etc.)
4. **Geometry:** Location information (coordinates)

**Coordinate Format:**
- **Important:** JSON uses [longitude, latitude] format
- This is opposite of common "latitude, longitude" convention
- Follows mathematical (x, y) convention

### Extracting All Earthquake Data

**Getting the List of Earthquakes:**
```python
import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))  # Should print 158
```

### Extracting Magnitudes

**Code Example:**
```python
all_eq_dicts = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])  # Print first 10 magnitudes
```

**Output:**
```
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
```

**Data Path Explanation:**
- `eq_dict`: Individual earthquake dictionary
- `['properties']`: Contains earthquake details
- `['mag']`: The magnitude value

### Extracting Location Data

**Complete Code:**
```python
all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]  # Longitude first
    lat = eq_dict['geometry']['coordinates'][1]  # Latitude second
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])
```

**Output:**
```
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
```

### Creating Your First World Map

**Basic Map Code:**
```python
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Data extraction code here...

# Map the earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
```

**Key Components:**
- `Scattergeo`: Chart type for geographic scatter plots
- `Layout`: Controls chart appearance
- `offline.plot()`: Creates HTML file with interactive map

### Alternative Data Specification Method

**Dictionary Format (More Flexible):**
```python
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
}]
```

**Advantages:**
- More explicit
- Easier to add customizations
- Better for complex styling

### Customizing Marker Sizes

**Size Based on Magnitude:**
```python
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],  # Scale factor of 5
    },
}]
```

**Explanation:**
- `'marker'`: Controls marker appearance
- `'size'`: List of sizes for each marker
- `5*mag`: Scale factor to make differences visible
- List comprehension creates size for each earthquake

### Customizing Marker Colors

**Complete Color Customization:**
```python
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,                          # Use magnitudes for color
        'colorscale': 'Viridis',               # Color scheme
        'reversescale': True,                  # Bright = low, Dark = high
        'colorbar': {'title': 'Magnitude'},   # Color bar label
    },
}]
```

**Color Parameters:**
- `'color'`: Data values for coloring
- `'colorscale'`: Color scheme name
- `'reversescale'`: Reverse color mapping
- `'colorbar'`: Color legend settings

### Available Color Scales

**Code to See All Options:**
```python
from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
    print(key)
```

**Popular Color Scales:**
- **Viridis**: Dark blue to bright yellow
- **Plasma**: Purple to yellow
- **Greys**: White to black
- **Blues**: Light blue to dark blue

### Adding Hover Text

**Complete Implementation:**
```python
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']  # Descriptive text
    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map with hover text
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,  # Custom hover text
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
```

**Hover Text Features:**
- Shows magnitude and location description
- Appears when mouse hovers over marker
- Provides detailed earthquake information

---

## Exercises: Try It Yourself (16-6 to 16-9)

### Exercise 16-6: Refactoring
**Goal:** Simplify the data extraction loop

**Original Code:**
```python
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
```

**Refactored Code:**
```python
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])
```

### Exercise 16-7: Automated Title
**Goal:** Extract title from metadata instead of hardcoding

**Solution:**
```python
# Extract title from metadata
dataset_title = all_eq_data['metadata']['title']
my_layout = Layout(title=dataset_title)
```

### Exercise 16-8: Recent Earthquakes
**Goal:** Download and visualize recent earthquake data

**Process:**
1. Visit https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
2. Choose a dataset (1-hour, 1-day, 7-day, or 30-day)
3. Download the JSON file
4. Modify your code to use the new data file
5. Create visualization

### Exercise 16-9: World Fires
**Goal:** Map global fire data using CSV format

**Approach:**
```python
import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Read fire data from CSV
filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Find relevant column indexes
    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    brightness_index = header_row.index('brightness')
    
    lats, lons, brightnesses = [], [], []
    for row in reader:
        lats.append(float(row[lat_index]))
        lons.append(float(row[lon_index]))
        brightnesses.append(float(row[brightness_index]))

# Create fire map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [brightness/50 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'Hot',
        'colorbar': {'title': 'Fire Brightness'},
    },
}]

my_layout = Layout(title='Global Fire Activity')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
```

---

## Key Concepts Summary

### CSV Processing
1. **Reading Files:** Use `csv.reader()` for automatic parsing
2. **Headers:** First row contains column descriptions
3. **Data Types:** Convert strings to appropriate types (`int()`, `float()`)
4. **Error Handling:** Use try-except for missing data

### Date Handling
1. **Conversion:** Use `datetime.strptime()` to convert strings
2. **Formatting:** Understand format codes (%Y, %m, %d)
3. **Plotting:** Use `fig.autofmt_xdate()` for readable date labels

### JSON Processing
1. **Loading:** Use `json.load()` and `json.dump()`
2. **Navigation:** Access nested data with bracket notation
3. **Structure:** Understand dictionaries and lists in JSON

### Visualization Best Practices
1. **Multiple Series:** Use different colors for different data types
2. **Transparency:** Use `alpha` parameter for overlapping elements
3. **Fill Areas:** Use `fill_between()` to show data ranges
4. **Interactive Maps:** Use Plotly for geographic data
5. **Customization:** Always add titles, labels, and legends

### Error Handling
1. **Missing Data:** Use try-except-else blocks
2. **Data Validation:** Check for empty strings and invalid values
3. **Graceful Failure:** Continue processing when some data is missing

---

## Final Notes

This chapter provides essential skills for data analysis:

1. **Real-world Data:** Most data has imperfections that need handling
2. **Format Flexibility:** CSV and JSON are extremely common formats
3. **Visualization Power:** Good charts communicate insights effectively
4. **Error Resilience:** Robust code handles missing or corrupt data
5. **Interactive Elements:** Modern visualizations should be interactive

These skills are fundamental for both hobby programming and professional data analysis work.
