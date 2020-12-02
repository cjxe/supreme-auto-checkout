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

**Do not forget** to install the necessary libraries.

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
1. Enter the "id" of the item you want to purchase.
2. Enter which shipping configuration you want to use.
3. Enter which card configuration oyu want to use. 

### To Do List
- [X] Load [config](https://github.com/cjxe/supreme-auto-checkout/tree/main/data) files into the app.
- [ ] Use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to scrape the data from the shop's website.
- [ ] Better error handling (possibly with requests library).
- [ ] Create a similar bot mainly using Requests instead of Selenium.

### Running the tests
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) is followed while coding this app.
- Checking out works at normal times.


