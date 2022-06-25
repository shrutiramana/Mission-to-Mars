#!/usr/bin/env python
# coding: utf-8


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment and set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping `functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres":hemisphere_details(browser)
        }
    
    #print("----------------------------")
    #print(data)
    #print("----------------------------")
    
    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # convert the browser html to a soup object and then quit the browser  different ways to get to the same result.

    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:

        slide_elem = news_soup.select_one('div.list_text')
        #slide_elem

        slide_elem.find('div', class_='content_title')
        #slide_elem.find_all('div')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()    

        # for getting the summary/paragraph of the article.
        news_summary = slide_elem.find('div',class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None   

    return news_title, news_summary

# ## JPL Space Images Featured Image


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)



    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        # img_url_rel
        
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'    

    #browser.quit()
    return img_url

def mars_facts():

    # since we need to keep the table structure of the scrapped html , we convert html into a dataframe using pandas.
    # read_html returns a list so to access data we need to refer to [0] element.
    # default columns are 0,1 & 2. so renaming columns and then creating an index.
    # Add try/except for error handling
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe

    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
  
    # convert dataframe into HTML format, add bootstrap

    new_html = df.to_html()
    return new_html

def hemisphere_details(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    
    hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

    for i in range(4):
        # Create the empty dictionary
        
        hemisphere = {}
        
        # Find and click to get to the full image button
        
        full_res_elem= browser.find_by_tag('h3')[i]
        full_res_elem.click()
        
        # Parse the resulting html with soup
        
        html = browser.html
        img_soup = soup(html, 'html.parser')
        
        # find the relative image url
        
        #img_url_rel = img_soup.find('img', class_='wide-image').get('src')
        url_atag = img_soup.find('div',class_='downloads')
        img_url_rel = url_atag.a['href']
        
        # Use the base url to create an absolute url
        
        image_url = f'https://marshemispheres.com/{img_url_rel}'
        
        # Use the parent element to find the first a tag and save it as news_title
        
        title = img_soup.find('h2', class_='title').get_text()
        hemisphere = {'img_url':image_url ,'title':title}
        hemisphere_image_urls.append(hemisphere)

        #navigate back to the beginning.
        browser.back()
   
    return hemisphere_image_urls

    
if __name__ == "__main__":
    # If running as script, print scraped data
    #print("----------------------------")
    print(scrape_all())
    #print("----------------------------")



