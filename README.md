# <span style="color:blue">AgentQL Meets Playwright: A New Era of Test Automation</span>


## AgentQL
AI-powered query language for **web scrapping**.

## Playwright
Playwright is a **powerful end-to-end testing framework** designed for modern web apps. It supports multiple browsers like **Chromium, Firefox, and WebKit** and works seamlessly in both **headless and headed modes**. But that’s not all—it also supports **API testing**, making it a complete solution for web automation

## Why This Combination?
Improves test reliability, reduces flaky tests, and speeds up scripting.

## What’s Covered in this tutorial:
  - Quick intro to **AgentQL's advantages**
  - **Step-by-step setup** (API key, environment setup, installation)
  - **Live Demo** using AgentQL with Playwright & Python

## What is Web scraping
Web scraping is the process of extracting data from websites automatically using scripts or tools. It involves fetching web pages, parsing their content (usually HTML), and extracting useful information. This data can then be stored, analyzed, or used for various purposes, such as market research, price comparison, lead generation, or automation.

**How Web Scraping Works:**

1. **Sending a Request** – A request is made to a website’s URL using tools like Python’s requests library or Selenium.
2. **Parsing HTML** – The retrieved HTML is parsed using libraries like BeautifulSoup (for static pages) or Selenium (for dynamic pages with JavaScript).
3. **Extracting Data** – The required information (e.g., product prices, article content, or stock prices) is identified using CSS selectors or XPath.
4. **Storing Data** – The extracted data is saved in formats like CSV, JSON, or databases for further processing.

## Why AgentQL?

- **No more fragile selectors**: Works without XPath or CSS Selectors.
- **Adapts to UI changes**: Even if the DOM structure changes, tests remain stable.
- **Human-readable queries**: Uses natural language instead of complex element locators.
- **Integrates with Playwright easily**: Runs across multiple browsers.
- **REST API support**: Can extract data even without a browser.

## Practical Setup

**Step 1: Getting an AgentQL API Key**

- Visit [**AgentQL website**](https://www.agentql.com/)
- Sign up and **generate an API key**

**Step 2: Adding the API Key to Environment Variable**

- AGENTQL_API_KEY "your-api-key-here"

**Step 3: Using the Agent QL and Playwright**

- **Install Playwright**

        pip install playwright
        
        playwright install

- **Install AgentQL**

        pip install agentql

