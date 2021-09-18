# Job Opportunity Assessment
## Versions and Libraries
This program uses Python version 3.9.7, BeautifulSoup version 4, and LXML

Beautiful Soup is a Python library for pulling data out of HTML and XML files.

LXML is an HTML and XML parser.

Beautiful Soup works with lxml parser to provide ways of navigating, searching, and modifying the parse tree.

## FormNamesJson

### About This File

**This file answers the first question or problem. To write a utility function that searches the website and retuns the product number and title of a specific form.**

To do this, you first "inspect" the website using the developer tools to find the raw data of how everything is writen and organized. This way you'd know what values to access in order to get the correct data back. 
The code takes input paramers for the form by defyning key value pairs in the payload function for returning the data, Then making declarations for the object key that will call to accessed on the table. For example, declaring the t_row as the value that would be equal to accessing data two to three or four levels deep (tr.td.a). 

This accesses the exact information from the raw data in the website and then by importin Json right at the top and using it in the print call, it grabs all the information that was just accessed and parses it as json in order to be more legible. 

To run the scipt, you simply type "python3 FormNamesJson.py" on terminal, or you can also just run the script in whatever program you use, and when the prompt appears, you enter the form name you are looking for. Example "form w-2" and it will print the data. 

##FormDwnlds
FormDwnlds follows the exact same code, except toward the end, it begins to change parameters in order to download the pdf file from the website. 

It makes a get request for the pdf link and then uses a .pdf trigger to grab the actual file link and convert it to a downloadble file. Which then gets downloaded when called upon at the end of the script. 

To download the form, when you run the script you would type the name of the form you want (as specified in the previous example), then you enter the year range, and the pdf is automatically downloaded to your subdirectory. Example. "form w-2, year range 2000 - 2012". 
