Cian.ru Apartment Listings Scraper

This Python script automates the process of loading and collecting apartment listings from Cian.ru
, specifically for flats for sale in Saint Petersburg. It uses Playwright to simulate human-like interaction with the website, clicking the “Показать ещё” (Show More) button until all listings are loaded.

Features

Loads multiple pages of apartment listings automatically.

Waits for the “Показать ещё” button to appear and clicks it repeatedly.

Introduces random delays between actions to mimic human behavior.

Prints the current number of loaded apartment cards to track progress.

Safe exit when no more listings are available.

Requirements

Python 3.9+

Playwright
 for Pythonit 