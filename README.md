# Twitter Tweet Monitor

This project is a Python script that monitors Twitter accounts for new tweets. It uses the Selenium library to automate web browsing and checks for updates in real-time. By providing a list of Twitter accounts to monitor, you can receive notifications whenever a new tweet is posted.

## Prerequisites

To run this script, you need to have the following installed:

- Python 3.x
- Selenium library
- ChromeDriver executable

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
   ```bash
   pip install selenium
   
3. Download the ChromeDriver executable and specify the path to it in the webdriver_path variable inside the script.
4. Configure the accounts to monitor by adding them to the config.txt file, with each account username on a new line.

## Usage
1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script by executing the following command:
   ```bash
   python tweet_monitor.py
   
3. The script will start monitoring the specified Twitter accounts and display any new tweets it detects.
4. You can customize the script behavior by modifying the time interval for checking updates or adding additional actions to perform when a new tweet is found.

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Licnese
This project is licensed under the MIT License.
