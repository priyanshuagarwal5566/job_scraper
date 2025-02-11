from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def scrape_indeed_jobs():
    url = "https://www.indeed.com/jobs?q=python+developer"

    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in the background
    options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    # Launch Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    time.sleep(3)  # Allow time for JavaScript to load content

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    jobs = soup.find_all("div", class_="job_seen_beacon")

    if not jobs:
        print("No jobs found. The page structure might have changed.")
    else:
        for job in jobs[:5]:  # Print first 5 jobs
            title = job.find("h2")
            print("Job Title:", title.text.strip() if title else "N/A")

scrape_indeed_jobs()
