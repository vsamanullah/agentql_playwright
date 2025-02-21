import os
import agentql
from playwright.sync_api import sync_playwright
from tkinter import messagebox




# Retrieve the API key from the environment variable
api_key = os.getenv("AGENTQL_API_KEY")
print(api_key)

if not api_key:
    raise ValueError("API Key not found! Please set the AGENTQL_API_KEY environment variable.")

# Configure AgentQL with the API key
agentql.configure(api_key=api_key)


# Example login automation with API key
URL = "https://opensource-demo.orangehrmlive.com/"

LOGIN_QUERY = """
{
    Username_input
    Password_input
    Login_btn
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = agentql.wrap(browser.new_page())  # Use the API key here

    # Navigate to the page
    page.goto(URL)

    # Query login elements
    response = page.query_elements(LOGIN_QUERY)

    # Fill login details
    response.Username_input.fill("Admin")
    response.Password_input.fill("admin123")

    # Submit the form
    response.Login_btn.click()

    # Wait for demo purposes
    page.wait_for_timeout(5000)

    messagebox.showinfo("Information", "This is a message box!")

    browser.close()
