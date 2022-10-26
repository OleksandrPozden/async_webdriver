from undetected_chromedriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import time
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
import asyncio

chrome_binary = ChromeDriverManager().install()
THREADS = 3
URLS = ["https://facebook.com","https://instagram.com","https://glassdoor.com","https://indeed.com","https://careerbliss.com","https://comparably.com","https://teamblind.com"]
def _get_page(url:str, lock=None):
    title = None
    with lock:
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = Chrome(service=Service(chrome_binary),options=chrome_options)
        driver.get(url)
        title = driver.title
    return title

async def get_page(url:str):
    loop = asyncio.get_running_loop()
    lock = Lock()
    content = await loop.run_in_executor(None,_get_page,url,lock) #  first arg specifies executor, if it is None - default is used
    return content

async def task(url):
    try:
        print("task is created")
        await asyncio.sleep(1) # sleeps for 1s
        title = await get_page(url)
        print(title)
    except Exception as e:
        print(e)


def main():
    executor = ThreadPoolExecutor(THREADS)
    loop = asyncio.get_event_loop()
    loop.set_default_executor(executor)
    pool_tasks = []
    for url in URLS:
        t = loop.create_task(task(url))
        pool_tasks.append(t)
    loop.run_forever()

if __name__=="__main__":
    main()
