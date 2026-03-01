# UFC Card Scraper and Stats Viewer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Libraries](https://img.shields.io/badge/Libraries-Requests%20%7C%20BeautifulSoup%20%7C%20Pandas-green)

A Python web scraping and data analysis tool that allows users to input any UFC event number, retrieves the full fight card from the official UFC website, and displays structured fight and fighter statistics.

The program extracts and presents:
- All matchups (red vs. blue corner)  
- Weight class  
- Results (method, round, time) for completed events  
- Detailed official fighter statistics (striking/takedown accuracy, per-minute rates, win methods, defense, etc.)

Future goal: Extend the project with a machine learning component to estimate win probabilities for upcoming fights based on historical fighter statistics.

---

## Project Design & Implementation

This project is built as a multi-stage data pipeline:

### Data Collection
- Uses **Requests** to retrieve UFC event and fighter profile pages  
- Uses **BeautifulSoup** to parse complex HTML structures and extract fight card and fighter statistics  

### Data Processing
- Organizes scraped information into structured formats using **Pandas**  
- Cleans and formats inconsistent or missing data from the UFC website  
- Separates event-level data (matchups, results) from fighter-level data (career statistics)  

### Program Flow
1. User enters a UFC event number through the command line  
2. The program constructs the corresponding event URL  
3. Fighter names are extracted from the fight card  
4. Each fighter’s individual statistics page is scraped  
5. Results are displayed in a clean, readable format  

---

## Motivation

I built this project to practice web scraping on a complex and dynamic website (ufc.com) and to develop a system that converts unstructured HTML data into structured, meaningful information.

The goal was to create a command-line tool that allows users to quickly view complete UFC event data and fighter statistics in one place.

This project also serves as a foundation for future data analysis and machine learning experiments using real-world sports data.

---

## Planned Extensions

This project will be expanded in future versions to include:

- Storing fight and fighter data in CSV format for further analysis  
- Performing statistical summaries (average fight time, win method distributions, fighter performance comparisons)  
- Visualizing results using Matplotlib  
- Adding a machine learning model to estimate win probabilities for upcoming fights based on historical data  

These extensions will transform the project from a scraper into a full data analysis and prediction pipeline.

---

## Current Status

- Successfully retrieves fight card details and comprehensive fighter statistics  
- Includes error handling for missing pages and incomplete data  

**Known Limitations**:
- Older events (pre-UFC 100) use different HTML structures and contain limited statistics, which may result in missing fields for some fights  
