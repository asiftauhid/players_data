# README: FIFA World Cup 2022 Players Data Scraper

## Project Overview
This project is a web scraper and API integration designed to collect information about the players of the national teams that participated in the 2022 Qatar FIFA World Cup. The project retrieves team and player data from the [Football-Data.org API](https://www.football-data.org) and scrapes market value information for players from the [Transfermarkt website](https://www.transfermarkt.com).

### Features
- Retrieves team and player details who participated in the 2022 FIFA World Cup.
- Scrapes player market value data from Transfermarkt.
- Merges API data and scraped data to produce a complete dataset of players.
- Cleans and formats the final dataset.
- Saves the cleaned dataset as a CSV file.

### Data Collected
- Player Names
- ID
- Player Positions
- Birth Dates
- Nationality
- Player Market Value (scraped from Transfermarkt)

## Prerequisites
Before running the script, ensure you have the following:

- Python 3.x
- Required libraries:
  - `requests`
  - `json`
  - `dotenv`
  - `os`
  - `BeautifulSoup`
  - `pandas`
  - `time`
  - `selenium`

## Setup Instructions
1. Clone this repository.
2. Navigate to the project directory.
3. Ensure you have an API key from [Football-Data.org](https://www.football-data.org) and store it in a `.env` file: `team_data_api=YOUR_API_KEY`
4. Install the required Python packages by running: `pip install -r requirements.txt`
5. Ensure you have a valid Chrome WebDriver installed and accessible from your PATH. You can download it from [here](https://chromedriver.chromium.org/downloads).

## Running the Scraper
To run the scraper, follow these steps:
1. Navigate to the project directory.
2. Run the following command: python main.py
3. The script will:
- Retrieve team and player data from the API.
- Prompt you to enter the name of the country for which you want player data.
- Scrape the Transfermarkt website for player market values.
- Merge and clean the data.
- Save the final dataset as a CSV file.

## Ethical Considerations

Please refer to our (ETHICS.md) file for guidelines on responsible and ethical web scraping practices.

## Disclaimer

This project is for educational purposes only. Ensure you comply with Transfermarkt website's terms of service and robots.txt file before deploying this scraper.



