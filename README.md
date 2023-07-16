# Web Scraping Script

This script uses Selenium and Python to scrape webpages, follow links, and save each webpage's source as an HTML file.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- Selenium
- Chrome WebDriver (compatible with your Chrome browser version)

## Installation

1. Clone this repository: `git clone https://github.com/Ikhsan121/scraping_html_pages.git`
2. Navigate to the project directory: `cd scraping_html_pages`
3. Install the required Python packages: `pip install -r requirements.txt`

## Running the Script Locally

1. Open a terminal or command prompt.
2. Navigate to the project directory if you haven't already: `cd scraping_html_pages`
3. Run the script: `python main.py`
4. The script will start scraping the webpages, following links, and saving each webpage as an HTML file in the `destwin_html_pages` folder.

## Running the Script Headless on Linux Server

1. Ensure you have a Linux server with a graphical interface or X server installed.
2. Connect to the Linux server via SSH with X11 forwarding enabled: `ssh -X user@your-server`
3. Follow the steps for running the script locally mentioned above.

## File Naming Convention

Each webpage will be saved as an HTML file in the `destwin_html_pages` folder. The filename will be derived from the URL with the following conventions:

- Slashes ("/") in the URL will be replaced by double hyphens ("--").
- The "https://" prefix can be skipped in the filename.

For example, the URL "https://example.com/path/to/page" will be saved as "destwin_html_pages/example.com--path--to--page.html".

## Contact

If you have any questions or issues, please feel free to contact me at [ikhsanarif211@gmail.com](mailto:ikhsanarif211@gmail.com).

