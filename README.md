
# Amazon Automation and Scraping using pytest, selenium

The project implements basic implementation of pytest for web automation
using selenium. 

### Functionalities implemented
- Basic Crawling
- Functional Testing
- Reporting
- Implement a script to crawl multiple pages of search results.

### Frameworks used 
- pytest
- Selenium
- Allure

# Installation 
setup venv
```{shell}
python3 -m venv venv
source ./venv/activate
```
Install requirements
```shell
pip install -r requirements.txt
```

# Running the project 
## Executing the scripts

### Setting parameters
All parameters for the test can be found in the `config.ini` file
```text
[data]
url = https://www.amazon.in/
productname = <product name to search>
filepath = <file to save output to>
crawlmaxpages = <number of pages to crawl per product>
```

```shell
pytest ./tests/test_amazon_automation.py -s -v --alluredir="./allure-reports"
```
The scraped output can be found in the `outputs` directory under `product_info.csv` file

## Viewing allure report
To view the coverage, logs and test execution view the allure report 
```shell
allure serve "./allure-reports" 
```

## Viewing logs 
All logs can be found in the `Logs` directory 