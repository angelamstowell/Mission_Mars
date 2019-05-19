# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser
def init_browser(): 
    
    exec_path = {'executable_path': '/app/.chromedriver/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():
    try: 

        #NASA Mars News
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        article = soup.find("div", class_='list_text')
        news_title = article.find("div", class_="content_title").text
        news_p = article.find("div", class_ ="article_teaser_body").text
        print(news_title)
        print(news_p)

        return mars_info

    finally:

        browser.quit()

# FEATURED IMAGE
def scrape_mars_image():

    try: 

       #JPL Mars Space Images - Featured Image
        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        html_image = browser.html
        soup = BeautifulSoup(html_image, 'html.parser')

        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = main_url + featured_image_url
        featured_image_url
        
        return mars_info
    finally:

        browser.quit()

        

# Mars Weather 
def scrape_mars_weather():

    try: 

            #Mars Weather
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)

        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        for tweet in latest_tweets: 
            weather_tweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weather_tweet:
                print(weather_tweet)
                break
            else: 
                pass
        
        return mars_info
    finally:

        browser.quit()


# Mars Facts
def scrape_mars_facts():

    #Mars Facts
    mars_facts_url = 'http://space-facts.com/mars/'

    mars_facts = pd.read_html(mars_facts_url)
    mars_df = mars_facts[0]

    mars_df.columns = ['Description','Value']
    mars_df.set_index('Description', inplace=True)
    mars_df.to_html() 
    data = mars_df.to_dict(orient='records') 
    mars_df

    return mars_info


# MARS HEMISPHERES


def scrape_mars_hemispheres():

    try: 

        #Mars Hemispheres
        base_hemisphere_url = "https://astrogeology.usgs.gov"
        hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemisphere_url)

        html_hemispheres = browser.html
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        items = soup.find_all('div', class_='item')
        
        hemisphere_image_urls = []

        hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in items: 
            
            title = i.find('h3').text

            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            browser.visit(hemispheres_main_url + partial_img_url)

            partial_img_html = browser.html
            
            soup = BeautifulSoup( partial_img_html, 'html.parser')

            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    # Display hemisphere_image_urls
        hemisphere_image_urls
        
        # Return mars_data dictionary 

        return mars_info
    finally:

        browser.quit()
