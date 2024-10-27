from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Initializing the webdriver
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

#Get the IMDb website page
driver.get("https://www.imdb.com/chart/top/")

#Click the detailed view button
detailed_button=driver.find_element(By.ID, "list-view-option-detailed")
time.sleep(5)
detailed_button.click()
time.sleep(5)

#Making the soup
soup=BeautifulSoup(driver.page_source,"html.parser")
# print(soup.title)

#Get the movie titles
title_elements=soup.select('.ipc-title__text ')
all_titles=[title.get_text() for title in title_elements]
titles=all_titles[2:252]
# print(titles)

#Get the movie release years
divs = soup.find_all("div",class_="sc-5bc66c50-5 hVarDB dli-title-metadata")
years = [div.find("span", class_="sc-5bc66c50-6 OOdsw dli-title-metadata-item").text for div in divs]
# print(years)

#Get the movie durations
durations = [div.find_all("span", class_="sc-5bc66c50-6 OOdsw dli-title-metadata-item")[1].text for div in divs]
# print(durations)

#Get the movie directors
directors_elements=soup.find_all("a",class_="ipc-link ipc-link--base dli-director-item")
directors=[director.get_text() for director in directors_elements]
# print(directors)

#Get the plotline of the movie
plot_elements=soup.find_all("div",class_="ipc-html-content-inner-div")
plots=[plot.get_text() for plot in plot_elements]
# print(plots)

#Get the movie ratings
ratings_elements = soup.select('.ipc-rating-star--rating')
ratings=[rating.get_text() for rating in ratings_elements] 
# print(ratings)

#close the current instance of the webdriver
driver.close()
 
#Looping through to fill the google form
for n in range(len(titles)):

    driver=webdriver.Chrome(options=chrome_options)
    driver.get("YOUR_GOOGLE_FORM_URL")
    
    #Select all the input fields
    title=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    year=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    director=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    plot=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    rating=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    duration=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    viewer=driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')

    #Input the values
    title.send_keys(titles[n])
    year.send_keys(years[n])
    director.send_keys(directors[n])
    plot.send_keys(plots[n])
    rating.send_keys(ratings[n])
    duration.send_keys(durations[n])
   
    #Click the submit button
    submit_button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    
    time.sleep(3)

    driver.quit()




