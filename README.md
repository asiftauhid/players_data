# FIFA World Cup 2022 Players Data Scraper

## Project Overview
The **FIFA World Cup 2022 Players Data Scraper** is a web scraping and API integration project that collects detailed information about the players of national teams that participated in the 2022 Qatar FIFA World Cup. The project combines player data retrieved from the [Football-Data.org API](https://www.football-data.org) with market value data scraped from the [Transfermarkt website]([https://www.transfermarkt.com](https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop). The end result is a clean and comprehensive dataset of FIFA World Cup players, including their market values.

## Features
- Retrieves team and player details who participated in the 2022 FIFA World Cup.
- Scrapes player market value data from Transfermarkt.
- Merges API data and scraped data to produce a complete dataset of players.
- Cleans and formats the final dataset.
- Saves the cleaned dataset as a CSV file.

## Data Collected
- Player Names
- Player IDs
- Player Positions
- Birth Dates
- Nationality
- Player Market Value (scraped from Transfermarkt)

## Why is This Dataset Valuable?
The dataset provides a unique combination of data that offers a comprehensive look at the players' details and market values, enabling football analysts, researchers, and enthusiasts to:

- **Explore correlations between player positions and market value** in the 2022 FIFA World Cup.
- **Explore correlations between players' age and market value** in the 2022 FIFA World Cup.
- **Assist in football scouting and recruitment** by providing financial metrics.
- **If detailed performance stats are added, it would help to analyze more factors that affect the market value**

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

1. Clone this repository:
   ```bash
   git clone https://github.com/asiftauhid/players_data.git
   ```

2. Navigate to the project directory:
   ```bash
   cd players_data
   ```

3. Ensure you have an API key from [Football-Data.org](https://www.football-data.org) and store it in a `.env` file in this format:
   ```bash
   team_data_api=YOUR_API_KEY
   ```

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Ensure you have a valid Chrome WebDriver installed and accessible from your PATH. You can download it from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) and move it to the project directory.

## Running the Scraper
To run the scraper and generate the dataset, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd players_data
   ```

2. Run the following command:
   ```bash
   python main.py
   ```

3. The script will:
   - Retrieve team and player data from the API.
   - Prompt you to enter the name of the country for which you want player data.
   - Run the web driver to simulate the click.
   - Scrape the Transfermarkt website for player market values.
   - Merge and clean the data.
   - Save the final dataset as a CSV file in the following format: `{country}_players_info.csv`

## Ethical Considerations

Please refer to our [ETHICS.md](./ETHICS.md) file for guidelines on responsible and ethical web scraping practices.

## Disclaimer

This project is for educational purposes only. Ensure you comply with Transfermarkt's terms of service and robots.txt file before deploying this scraper.

## Project Structure

```
FIFA-WorldCup-2022-Player-Scraper/
│
├── main.py                  # The main Python script for the project
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
├── ETHICS.md                # Ethical considerations
├── .env                     # Stores API key (not included in the repo)
└── {country}_players_info.csv  # Example of the cleaned dataset output
```

---
