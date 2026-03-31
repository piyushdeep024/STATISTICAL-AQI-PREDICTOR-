# V-AIR: Statistical AQI Predictor

**CSE Project - VIT Bhopal**  
**Student:** Piyush Deep  
**Registration No:** 25BAI11280  
**Professor:** DR. MK Jayanthi  
**Course:** Computer Science & Engineering  

---

##  Project Overview

V-AIR is an interactive **Air Quality Index (AQI) prediction system** that uses **linear regression** to forecast future AQI values based on historical hourly readings. The system provides real-time data entry, categorization, statistical analysis, and trend visualization.

**Key Features:**
- Interactive menu-driven interface
- Automatic AQI categorization (Good → Hazardous)
- Linear regression-based prediction
- Historical data visualization with trend lines
- Maximum 100 records storage capacity

---

##  Tech Stack
Python 3.x
├── NumPy (Statistical computations)               
├── Matplotlib (Data visualization)      
└── Dataclasses (Data modeling)      

---

##  Pseudo Code
ALGORITHM V-AIR_AQI_Predictor

1. INITIALIZE:
records = empty list
MAX_RECORDS = 100

2. WHILE user wants to continue:    
DISPLAY menu (1-5 options)    
GET user choice IF choice == 1: // Add Reading    
IF records >= MAX_RECORDS:    
DISPLAY "Database full"    
ELSE:    
GET aqi_value from user   
hour = length(records) + 1    
category = classify_AQI(aqi_value)    
ADD AirQualityRecord(hour, aqi_value, category) to records IF choice == 2: // Show History    
IF records empty:   
DISPLAY "No data"   
ELSE:    
DISPLAY table: hour, AQI, category for all records IF choice == 3: // Predict     
IF records < 2:      
DISPLAY "Need minimum 2 points"    
ELSE:      
x = array of hours   
y = array of AQI values    
m = slope = (n∑xy - ∑x∑y) / (n∑x² - (∑x)²)    
c = intercept = (∑y - m∑x) / n    
next_aqi = m*(max_hour+1) + c    
DISPLAY prediction results IF choice == 4: // Plot    
PLOT scatter(x,y) + trend_line(mx + c) IF choice == 5:   
EXIT   

END WHILE   

---

##  Workflow Flowchart
START     
↓ [Initialize System]      
↓ ┌─────────────────────┐      
│ MAIN MENU │     
│ 1.Add 2.History │──────┐     
│ 3.Predict 4.Graph │ │    
│ 5.Exit │ │     
└─────────────────────┘ │   
↓ │   
┌─────────────────┐ │    
│ Add Reading │◄─────────┘    
│ (AQI Input) │    
└─────────────────┘    
↓ ┌─────────────────┐    
│ Store Record │    
│(Hour+AQI+Cat) │    
└─────────────────┘   
↑ └──────────────────────┐    
↓      
┌──────────────┐        
│ HISTORY │    
│ DISPLAY │     
└──────────────┘    
↓     
┌──────────────┐    
│ PREDICT │───► [Linear Regression]     
│ (m,c) │ ↓      
└──────────────┘ [Next Hour AQI]     
↓ ↑    
┌──────────────┐ │    
│ GRAPH │◄──┘    
│ (Trendline) │   
└──────────────┘    
↓    
[Back to Menu]    
↓    
[EXIT?]      

---

##  How to Run

```bash
# Clone/Download the project
git clone <your-repo-url>
cd v-air-aqi-predictor

# Run the application
python aqi_predictor.py
```

**Sample Usage:**
===== MENU =====

1. Add AQI Reading

2. Show History

3. Predict AQI

4. Show Graph

5. Exit
Enter choice: 1
Enter AQI value: 45
[✓] Reading added successfully.

---

##  AQI Categories

| AQI Range | Category       | Color Code |
|-----------|----------------|------------|
| 0-50      | GOOD           |  Green   |
| 51-100    | MODERATE       |  Yellow  |
| 101-200   | UNHEALTHY      |  Orange  |
| 201-300   | VERY UNHEALTHY |  Red     |
| 300+      | HAZARDOUS      |  Purple  |

---

##  Algorithm Details

### Linear Regression Formula
y = mx + c

Where:
m (slope) = (n∑xy - ∑x∑y) / (n∑x² - (∑x)²)
c (intercept) = (∑y - m∑x) / n
Prediction = m × (next_hour) + c

**Time Complexity:** O(n) for prediction  
**Space Complexity:** O(n) for storing records

---

##  Sample Output
HOUR AQI CATEGORY     

1 45.00 GOOD    
2 67.50 MODERATE    
3 89.20 MODERATE    

--- Prediction Result ---   
Slope (m): 22.35    
Intercept (c): 12.45    
Next Hour AQI: 111.80   
Category: UNHEALTHY    

---

##  Future Enhancements

- [ ] Multiple pollutants (PM2.5, PM10, NO2, etc.)
- [ ] Machine Learning models (LSTM, Random Forest)
- [ ] Real-time API integration (AQI.in, OpenWeather)
- [ ] Web Dashboard (Flask/Django)
- [ ] Export data (CSV, JSON)
- [ ] Confidence intervals for predictions

---

##  Academic Contributions

1. **Data Structures:** Efficient list-based storage with dataclasses
2. **Algorithms:** Manual linear regression implementation
3. **OOP Principles:** Encapsulation, static methods
4. **Visualization:** Matplotlib trend analysis
5. **Error Handling:** Input validation & edge cases

---

VIT Bhopal CSE Department
Professor: MK Jayanthi

---

**Thank you for reviewing my project!**  
**Piyush Deep**  
**25BAI11280**  
**piyushdeep481@gmail.com**
