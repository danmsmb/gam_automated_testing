GAM UAT Automation

End-to-end UAT automation for the GAM platform, built with Playwright + Pytest + Allure + pytest-bdd.
This suite validates Citizen and Admin flows and generates an Allure evidence report.

1. Prerequisites
Python 3.10+ installed
pip (comes with Python)
Git (to clone the repository)

2. Setup
Clone the repo
git clone https://github.com/danmsmb/gam_automated_testing.git
cd gam_automated_testing

Create a virtual environment
python -m venv .venv
.venv\Scripts\activate    # Windows PowerShell

Install dependencies
pip install -U pip
pip install -r requirements.txt

Install Playwright browsers
python -m playwright install

3. Running Tests
Run the full suite
pytest -p no:allure_pytest tests/step_definitions --browser chromium -vv --headed --alluredir=allure-results

Explanation
-p no:allure_pytest → disables duplicate allure hooks if needed
--browser chromium → runs tests on Chromium
-vv → verbose output
--headed → shows browser UI (remove for headless)
--alluredir=allure-results → saves results for the Allure report

4. Viewing Reports
After running the suite, generate and view the Allure report:
allure serve allure-results

This will open a browser with the interactive report (test titles, steps, screenshots).

5. Key Packages Used
pytest
playwright
pytest-playwright
allure-pytest
pytest-bdd

6. Notes
Use .venv for isolation.
Do not commit allure-results/ or .venv/ (already in .gitignore).
For non-technical users, a packaged UAT Evidence Report (Word/PDF) is available in /docs.
