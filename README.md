# Automated checkout for Supreme 👕


<p align="center">
	*demonstration*
</p>

<p align="center">
  <img src="https://i.ibb.co/9yZzmNx/ezgif-com-gif-maker.gif">
</p>

<p align="center">
	(Card details are not real!)
</p>

## Features
- [X] Search function to find the item.
- [X] Category selection. (BONUS)
- [X] Style/colour selection.
- [X] Size selection.
- [X] Load different shipping/billing & card profiles.
- [X] Does not scam you.

## Getting Started
Python and a few libraries are necessary to run the file.

### Prerequisites
- [Python 3.8](https://www.python.org/downloads/) or newer
	- [Selenium](https://selenium-python.readthedocs.io/)
	- [Requests](https://requests.readthedocs.io/en/master/)
	- [termcolor](https://pypi.org/project/termcolor/)

### Installing
[Click here](https://github.com/cjxe/supreme-auto-checkout/archive/main.zip) to download **or** copy 
```
git clone https://github.com/cjxe/papajohnsTR-auto-checkout
``` 
and right click on the command-line to paste.

⚠️ **Do not forget** to install the necessary libraries.

- To install the dependencies, copy:
```
pip install -r requirements.txt
```
and paste on the command-line.

### Usage
![console](https://i.ibb.co/1TPn4kR/how-to-use.png)

0. After installing Python and the necessary libraries, double click `main.py`.
1. Enter which shipping configuration you want to use (i.e  for shipping_1, enter 1).
2. Enter which card configuration you want to use (i.e  for card_1, enter 1). 
3. Enter category (i.e  Jackets).
4. Enter keyword(s) (i.e  Script, Wool).
5. Enter a colour (i.e  Purple).
6. Enter a list of different sizes (i.e  S, XL, M).

### To Do List
- [X] ~~Find item by id.~~ *(Replaced by "find item by keywords")*
- [X] Load [profile/config](https://github.com/cjxe/supreme-auto-checkout/tree/main/data) files into the bot.
- [X] Use**d** ~~[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)~~ Selenium and JSON to scrape the data from shop's website.
- [X] Make a search function which takes a list of words and then looks up in the JSON data and finds the item.
- [X] Add size selection.
- [X] Accept a list of sizes and iteratively try every size until the bot finds one in stock.
- [X] Add style/colour selection.
- [ ] Accept a list of colours and iteratively try every colour until the bot finds one in stock.
- [X] Fancy the terminal. *(added colour)*
- [ ] Enter shipping & card details using JavaScript.
- [ ] If found CAPTCHA, wait until it is solved.
- [ ] Better error handling (possibly with requests library).
- [ ] Create a similar bot mainly using Requests instead of Selenium.

### Running the tests
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) is followed while coding this app.
- Checking out works at normal times.

### Found a bug or want to contribute?
- For bugs and requests please create a new issue [here](https://github.com/cjxe/supreme-auto-checkout/issues).

#### USE AT YOUR OWN RISK!!
[![HitCount](http://hits.dwyl.com/cjxe/supreme-auto-checkout.svg)](http://hits.dwyl.com/cjxe/supreme-auto-checkout)