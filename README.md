# Mission-to-Mars

## Overview of project 
### Purpose 
Is to build a web application using BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, and to display the data on the web - app.

### Resources 
1. websites scraped - 'https://redplanetscience.com'
                 -'https://spaceimages-mars.com' 
                 - 'https://galaxyfacts-mars.com
                 - 'https://marshemispheres.com/
                 
2. Python 
3. VS code
4. Beautiful Soup 
5. Splinter 
6. MongoDB
7. Flask 
8. Bootstrap
           
### Deliverable 1 & 2 :  Scrape Full-Resolution Mars Hemisphere Images and Titles /  Update the Web App with Mars’s Hemisphere Images and Titles.
- Code to retrieve the full-resolution image and titles for each hemisphere image
- Then a dictionary of image and title for each hemisphere is stored in a dictionary.
- A list of dictionary with image and title for each hemisphere image is created as below 
- Scraping.py is modified to accomodate the mars hemisphere information (url & title) 
- Database is updated to contain the infomation retrieved
- index.html is modified to display the Mars hemisphere (image and its title).

<img width="1140" alt="url" src="https://user-images.githubusercontent.com/98556229/175799732-bcbab4a9-ef08-40d8-abd8-fe891a638048.png">

![mars_del1](https://user-images.githubusercontent.com/98556229/175799771-7f5ac50d-acde-458a-8716-dec789323d7c.png)

<img width="514" alt="mongo_db" src="https://user-images.githubusercontent.com/98556229/175799844-119ca947-7374-45c3-a66e-a9885aed1f6a.png">

### Deliverable 3 :  Add Bootstrap 3 Components.
- The Mars hemisphere images are changed using Bootsrap3 to be in same row. 
<img width="1432" alt="sidebyside" src="https://user-images.githubusercontent.com/98556229/175799975-aeeddbe1-c00a-484c-8c11-a600a575f280.png">


- The webpage is mobile-responsive - below are the screenshots for ipad-Air ,iphone 12 pro.

<img width="822" alt="ipad_air" src="https://user-images.githubusercontent.com/98556229/175799979-5b048224-c69a-4d8b-8318-9f77d33d0af5.png">
<img width="549" alt="iphone 12pro" src="https://user-images.githubusercontent.com/98556229/175799990-b0a9022f-6e1d-4651-bdd8-ca8d0c7194c1.png">

- Two additional Bootstrap 3 components are used to style the webpage - 
    -  changing the color of the "Scrape New Button" - to Green , White Font and it hightlights when we hover over it.
    
    <img width="607" alt="image" src="https://user-images.githubusercontent.com/98556229/175800034-735bfa42-ce32-4b75-9ff6-3d0047d40806.png">
    
    -  Adding color to the alternate row of the Mars Facts table to add more asthetics to it.
    
    <img width="1275" alt="image" src="https://user-images.githubusercontent.com/98556229/175800061-807431b7-c9ec-4acb-be3c-e98c670b70b6.png">


### Summary 
Successfully scraped data to get Mars information using beautiful soup and splinter and stored in MongoDb.


