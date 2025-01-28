# Selenium_Assessment
Automating the table searching using the Selenium with Python.

# Performming test for Table Search Functionality
This project automates the validation of the search functionality on the **Selenium Playground Table Search Demo** website using Selenium WebDriver with Python.

## Objective
The script tests the search functionality on the table by searching for "New York" and validates that:
- The results show 5 entries out of the 24 available entries.
- The number of rows displayed matches the expected value.

## Setup Instructions
1. **Install dependencies**:
    - Make sure you have Python 3.x installed.
    - Install Selenium and pytest using pip command:
    ```bash
    pip install pytest
    pip install selenium
    ```

2. **WebDriver**:
    - Download the ChromeDriver from [ChromeDriver](https://sites.google.com/chromium.org/driver/).
    - Ensure that the WebDriver is compatible with your browser version and is added to your system’s PATH.

## Running the Test
1. Open the project in PyCharm:

Using PyCharm, open your project and navigate to the script qa_selenium_test.py.
Run the Test using Pytest:
2. In Pycahrm Terminal run this command 
"Pytest script qa_selenium_test.py -v -s"

3. Test Execution:
The script will launch Google Chrome ,navigate to the Selenium Playground Table Search Demo page, perform the search for "New York", and validate the results.
If the assertions pass, the test will be successful. If any assertion fails, the test will provide feedback about the failure.

## Notes:
- Ensure that your Chrome or Firefox browser version is compatible with the WebDriver.
- The script can be modified to run in other browsers if necessary.

