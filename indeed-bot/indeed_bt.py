from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re
import requests


# Create Chrome Options instance
chrome_options = Options()

# Add any desired options, such as user-agent or headless mode
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# Initialize the Chrome driver with the Options instance
driver = webdriver.Chrome(options=chrome_options)

# navigate to the Indeed website
driver.get("https://www.indeed.com/jobs?q=Data+Scientist&l=New+York&start=0")

