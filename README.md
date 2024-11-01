# IMDb Scraper and Google Forms Automation

This project scrapes movie data from the IMDb Top 250 Movies list and submits the data to a Google Form using Selenium and BeautifulSoup.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Required Python packages: `selenium`, `beautifulsoup4`
   
## Installation

Before you begin, ensure you have the following installed on your machine:

1. **Python 3.x**: Make sure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).

2. **Google Chrome browser**: The script requires the Chrome browser. Download it from [here](https://www.google.com/chrome/).

3. **ChromeDriver**: This is necessary for Selenium to control Chrome. Make sure the version of ChromeDriver matches your installed Chrome version. You can download it from the [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).

4. **Required Python packages**: Use `pip` to install the necessary packages by running:
   ```bash
   pip install selenium beautifulsoup4

## Usage

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd IMDb-scraping
2. Configure the Script:

    - Open the script file app.py in a text editor
    
    - Replace YOUR_GOOGLE_FORM_URL with the URL of your Google Form where you want to submit the data
3. Run the Script:
   
         python app.py
4. Process:

      - The script will scrape the IMDb Top 250 Movies data, including titles, release years, directors, plotlines, ratings, durations, and viewer counts.
      - It will automatically submit this data to the specified Google Form.

### Customization
- Make sure to replace `<repository-url>` with the actual URL of your repository.
- Feel free to adjust any text or formatting to better fit your project's style or requirements!

