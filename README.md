# Automated checkout for Supreme 👕

## Getting Started
Python and a few libraries are necessary to run the file.

### Prerequisites
- [Python 3.8](https://www.python.org/downloads/) or newer
	- [Selenium](https://selenium-python.readthedocs.io/)
	- [Requests](https://requests.readthedocs.io/en/master/)

### Installing
[Click here](https://github.com/cjxe/supreme-auto-checkout/archive/main.zip) to download **or** copy 
```
git clone https://github.com/cjxe/papajohnsTR-auto-checkout
``` 
and right click on the command-line to paste.

⚠️ **Do not forget** to install the necessary libraries.

- To install selenium:
```
pip install selenium
```

- To install requests:
```
pip install requests
```

### Running the file
![console](https://i.ibb.co/1TPn4kR/how-to-use.png)
1. Enter which shipping configuration you want to use (i.e  1).
2. Enter which card configuration you want to use (i.e  1). 
3. Enter category (i.e  Pants).
4. Enter keyword(s) (i.e  Cargo).
5. Enter size (i.e L).

### To Do List
- [X] Load [config](https://github.com/cjxe/supreme-auto-checkout/tree/main/data) files into the app.
- [X] Use**d** ~~[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)~~ Selenium and JSON to scrape the data from the shop's website.
- [X] Make a search function which takes a list of words and then looks up in the json data and finds the item.
- [X] Add size selection.
- [ ] Accept a list of sizes and iteratively try every size until the bot finds one in stock.
- [ ] Better error handling (possibly with requests library).
- [ ] Create a similar bot mainly using Requests instead of Selenium.

### Running the tests
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) is followed while coding this app.
- Checking out works at normal times.

#### USE AT YOUR OWN RISK!!
