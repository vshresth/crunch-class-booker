from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# 👇 Secure credentials from environment variables
EMAIL = os.getenv("CRUNCH_EMAIL")
PASSWORD = os.getenv("CRUNCH_PASSWORD")

# 👇 Weekly class schedule (22 hours in advance)
SCHEDULE = {
    "Monday":    {"name": "Foundation", "time": "7:00 PM"},
    "Wednesday": {"name": "Flow",       "time": "7:30 PM"},
    "Thursday":  {"name": "Flow",       "time": "5:30 PM"},
    "Friday":    {"name": "Flow",       "time": "8:00 AM"},
    "Saturday":  {"name": "Foundation", "time": "8:00 AM"},
    "Sunday":    {"name": "Flow",       "time": "10:00 AM"},
}

def get_today_target_class():
    today = datetime.now().strftime("%A")
    return SCHEDULE.get(today)

def book_class():
    class_info = get_today_target_class()
    if not class_info:
        print("No class scheduled for today.")
        return

    class_name = class_info['name']
    class_time = class_info['time']
    full_text = f"{class_name} {class_time}"
    print(f"Trying to book: {full_text}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            print("Logging into Crunch...")
            page.goto("https://www.crunch.com/login")
            page.fill("input[name='email']", EMAIL)
            page.fill("input[name='password']", PASSWORD)
            page.click("button[type='submit']")
            page.wait_for_load_state("networkidle")

            print("Navigating to schedule...")
            page.goto("https://www.crunch.com/your-schedule")
            page.wait_for_load_state("networkidle")

            print(f"Looking for class: {full_text}")
            page.click(f"text={full_text}")

            # 👇 Uncomment for real booking:
            # page.click("button:has-text('Book Now')")

            print("Booking successful (dry run).")
        except Exception as e:
            print("Booking failed:", e)
        finally:
            browser.close()

if __name__ == "__main__":
    book_class()
from playwright.sync_api import sync_playwright
from datetime import datetime
import os

# 👇 Secure credentials from environment variables
EMAIL = os.getenv("CRUNCH_EMAIL")
PASSWORD = os.getenv("CRUNCH_PASSWORD")

# 👇 Weekly class schedule (22 hours in advance)
SCHEDULE = {
    "Monday":    {"name": "Foundation", "time": "7:00 PM"},
    "Wednesday": {"name": "Flow",       "time": "7:30 PM"},
    "Thursday":  {"name": "Flow",       "time": "5:30 PM"},
    "Friday":    {"name": "Flow",       "time": "8:00 AM"},
    "Saturday":  {"name": "Foundation", "time": "8:00 AM"},
    "Sunday":    {"name": "Flow",       "time": "10:00 AM"},
}

def get_today_target_class():
    today = datetime.now().strftime("%A")
    return SCHEDULE.get(today)

def book_class():
    class_info = get_today_target_class()
    if not class_info:
        print("No class scheduled for today.")
        return

    class_name = class_info['name']
    class_time = class_info['time']
    full_text = f"{class_name} {class_time}"
    print(f"Trying to book: {full_text}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            print("Logging into Crunch...")
            page.goto("https://www.crunch.com/login")
            page.fill("input[name='email']", EMAIL)
            page.fill("input[name='password']", PASSWORD)
            page.click("button[type='submit']")
            page.wait_for_load_state("networkidle")

            print("Navigating to schedule...")
            page.goto("https://www.crunch.com/your-schedule")
            page.wait_for_load_state("networkidle")

            print(f"Looking for class: {full_text}")
            page.click(f"text={full_text}")

            # 👇 Uncomment for real booking:
            # page.click("button:has-text('Book Now')")

            print("Booking successful (dry run).")
        except Exception as e:
            print("Booking failed:", e)
        finally:
            browser.close()

if __name__ == "__main__":
    book_class()
