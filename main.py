import requests
import json
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def load_api():
    #getting secret api key
    load_dotenv()
    team_data_api = os.getenv("team_data_api")

    #definign api url and key
    url = "http://api.football-data.org/v4/competitions/WC/teams"
    api_key = team_data_api

    #the headers
    headers = {
        "X-Auth-Token": api_key
    }

    #requesting to get the api
    response = requests.get(url, headers=headers)

    # retrieves data if the runcode in 200
    if response.status_code == 200:
        teams_data = response.json()
        return teams_data
    else:
        print(f"Failed to get data from the api. Error code: {response.status_code}")
    
def load_country_names(data):
    country_cnt = 1
    #iterates through each team to get the counry name
    for team in data['teams']:
        country_names = team['area']['name']
        print(f'{country_cnt}. {country_names}')
        country_cnt = country_cnt + 1

def load_player_data(data, country):
    #iterates through each team to get the json file for the player details list
    for team in data['teams']:
        if team['area']['name'].lower() == country.lower():
            player_dets = team['squad']
            return player_dets


def load_player_value():
    #calling webdriver
    driver = webdriver.Chrome()

    # url to the webpage that will be scrapped
    url_2 = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop'
    driver.get(url_2)
    #time gap to let the page load and manually clicking the accept button
    time.sleep(5)

    '''accept_button = driver.find_element(By.XPATH, '//button[@title="Accept & continue"]')
    accept_button.click()'''

    #declaring list to hold the player name along with their market value
    players = []


    # Loop through the pages
    cnt = 1
    for page in range(1, 21):  # there are 20 pages for 500 players on the webpage
        try:
            #loading time
            time.sleep(3)

            #scrolling 3/5th of the page 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 3 / 5);")

            #scrolling time
            time.sleep(3)

            #parse the current page content with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            #scrape data
            for row in soup.find_all('tr', class_='odd') + soup.find_all('tr', class_='even'):
                player_name = row.find('td', class_='hauptlink').get_text().strip()
                market_value = row.find('td', class_='rechts').get_text().strip()
                players.append({'Player': player_name, 'Market Value': market_value})

            print(f'Successfully scraped page {cnt}')

            #attempt to click the next button untill it's 20th page
            if cnt==20:
                break
            try:
                next_button = driver.find_element(By.XPATH, '//a[@title="Go to the next page"]')
                next_button.click()
            except Exception as e:
                print(f"No next button found or error clicking on page {cnt}. Error: {e}")
                continue
                
            cnt += 1

        except Exception as e:
            print(f"Error on page {cnt}: {e}")
            continue
            
    return players

def run_cleaning(data):
    #deleting extra column
    data.drop('Player', axis=1, inplace=True)
    #renaming all the columns
    data.rename(columns={'id':'ID', 'name':'NAME', 'position':'POSITION','dateOfBirth':'BIRTH DATE', 'nationality': 'NATIONALITY', 'Market Value':'MARKET VALUE'}, inplace=True)
    #positioning Name column to the front
    data.columns = ['ID', 'NAME', 'POSITION', 'BIRTH DATE', 'NATIONALITY', 'MARKET VALUE']
    data = data[['NAME', 'ID', 'POSITION', 'BIRTH DATE', 'NATIONALITY', 'MARKET VALUE']]
    #replacing the empty spaces with Unknown of the Market Value column
    data['MARKET VALUE'].fillna('Unknown', inplace=True)

    return data

def main():
    print("\nList of the countries that participated in the 2022 Qatar World Cup: \n")
    #loading the api and getting the entire dataset
    data = load_api()

    #calling the funtion to get only names 
    country_names = load_country_names(data)

    #taking input to return data for specific country
    country  = input("\nEnter the country name you want the data for!!\n>>")
    #calling function to get players data from the api for the specific country
    players_data = load_player_data(data,country)
    #converting players_data to list from json
    df_players = pd.DataFrame(players_data)

    #calling function to scrape data about market value
    players_value = load_player_value()
    #converting to list
    df_values = pd.DataFrame(players_value)

    #merging both of the data frame
    merged_df = pd.merge(df_players, df_values[['Player', 'Market Value']], left_on='name', right_on='Player', how='left')

    #calling function to do necessary cleaning
    cleaned_data = run_cleaning(merged_df)
    #print(cleaned_data)
    #exporting the data as a .csv file
    cleaned_data.to_csv(f"{country}_players_info.csv", index=False)
    print(f"\nCleaned data was successfully saved as {country}_players_info.csv at last!!😩😩")

if __name__ == "__main__":
    main()