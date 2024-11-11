from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import time
import random

# Konfigurasi proxy dengan autentikasi (replace with your actual credentials)
proxy_host = "rp.proxyscrape.com"  # Replace with your proxy host
proxy_port = "6060"               # Replace with your proxy port
proxy_user = "dckcrm5leu7puc5-session-bfxqbn9zqx-lifetime-5"  # Replace with your proxy username
proxy_pass = "758ror8d8ozn56e"  # Replace with your proxy password

def visit_website(delay=5):
    while True:
        try:
            # Menghasilkan user-agent acak
            user_agent = UserAgent().random
            proxy_options = {
                'proxy': {
                    'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                    'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
                    'no_proxy': 'localhost,127.0.0.1'
                }
            }

            # Mengatur opsi Chrome
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f"user-agent={user_agent}")
            chrome_options.add_argument("--headless")  # Mode headless
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            # Memulai driver dengan opsi headless, proxy, dan user-agent
            driver = webdriver.Chrome(seleniumwire_options=proxy_options, options=chrome_options)

            # Buka website utama dan tunggu sampai halaman dimuat
            driver.get("https://www.profitablecpmrate.com/j3164ikjx7?key=d1f89719d6c832d7f2ee2d3d0e1ffe74")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print(f"Website loaded successfully with user-agent: {user_agent}")

            # Simulate user behavior (optional)
            # Add code here to interact with the website elements in a way that mimics human browsing
            # This helps prevent detection by anti-scraping measures

            # Extract desired data (if applicable)
            # Add code here to extract the data you're interested in from the website

        except Exception as e:
            print(f"An error occurred:", e)

        finally:
            driver.quit()

        # Random delay to avoid suspicion (optional)
        time.sleep(delay + random.uniform(0, 3))  # Add a random delay between 5 and 8 seconds

# Menjalankan fungsi untuk mengunjungi website
if __name__ == "__main__":
    visit_website(delay=5)
