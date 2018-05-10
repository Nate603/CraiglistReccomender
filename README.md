# 612-Project
Read Me

For our project, it takes in many arguments. The make and model are required as well as the zipcode. If you run the program too many times then craigslist blocks your ip address. An attempt was made to fix this using rotating proxies and a fake-useragent but is still unresolved. This was one of our biggest problems as if you get locked out you had to wait almost 24 hours until making another request. The picture below is our initial recommendations csv that contains all the data grabbed from craigslist. This includes the date, title, link, price, year, make, model, miles, color, fuel type, vin, title status, car type, transmission, size, drive, cylinders, and condition. Some of the data could not be found because the seller did not include it in the description and info. 



The picture below is noduplicates csv file that contains only the unique data from the initial recommendations csv file. This is because there were many duplicates that the craigslist seller included. The noduplicates csv file also includes recommended price from cargurus.com that we grabbed as well as a indicator saying good or bad price if the craigslist price is higher or lower than the recommended price if there was one. The last column is the price difference of the craigslist price and the cargurus price.






Visualization of recommendations
This graph shows the Craigslist Price of Nissan Maximas compared to the Recommended Price on cargurus.com. The graph does not contain an equal amount of craigslist prices to recommended prices because carguru database did not contain the information on the cars being passed in. This originally through an error, but we created an IF statement that would instead write ?not enough data? or ?bad data?. Also we ran into a problem when plotting the prices because one of the prices was extremely high, which caused the other bar charts to not show up. To fix this we had to remove the number from the csv file. We could potentially look for abnormally larger prices such as this one to prevent this from happening(or data that seems bad in general).



How Program Works

1. Type in arguments using argparse
2. Grabs data from craigslist depending on arguments, use requests in python to send a request using the users parameters
3. Web scraper using beautifulsoup library in python, scrapes information from each posted add and exports the data to ?initialrecommenedations.csv? file
4. ?Initialrecommendations.csv? is then sent through another python program that removes the duplicate listings and exports this to a file called ?noduplicates.csv?
5. From the ?nodplicates.csv? file we used a python library called selenium that can auto fill forms on the web. We took the data from the ?noduplicates.csv? file and write this data to the web form(we used cargurus, that gives you an estimated car value based on certain information) and get a estimated price for that specific car
6. We then compare this price to the price on craigslist for each listing and made a visualization(just a bar chart for now) using the matplot library in python. This graph compares the price from craigslist and the carguru price for each listing. 
7. We then have a simple bash script called ?move.sh? that creates a directory each time you use the program. The directory is named by the user parameters and we move both the ?initialrecommendations.csv? file and the ?noduplicates.csv? file into this directory.

Libraries Used in Python, some had to be installed
-Selenium: auto filling forms, need to change the path of selenium in formsubmitter.py
-BeautfulSoup: web scraping
-Matplotlib: for visualization 



Bash
-Created little script that creates a directory and names it depending on the users arguments. Then moves the two files created to the directory
 ÿ
Possible Future Work
-Could potentially scrape more data from craigslist so that our price recommendations are more accurate. Could scrape the description and look for certain data such as car trim. Right now we just default to the first trim level.
-Also the carguru evaluator form has some drop down menus, so you can?t just type in values. Sometimes the data is not in the correct format so it does not find these values in the drop down menu.


