<h1 align="left">:computer: IntervaloTecnico-PythonSelenium  </h1>
Simple web testing project to be taught and used in a workshop using Selenium and Python.

## Introduction
This project contains an automated test suite example for the Login page from the website <a href="http://automationpractice.com/index.php?controller=contact">Automation Practice</a> to be used in a workshop.

## Environment Setup
**Prerequisites:** 
* Python 3+ 
* pip3
* Chrome webdriver 
* PyCharm or similar IDE

Check the webdriver documentation:
- Chrome: https://chromedriver.chromium.org/getting-started

1. Create and activate virtualenv
```
virtualenv --python=/usr/bin/python3.7 selenium_python 
```
```
source selenium_python/bin/activate
```

2. Install the requirements:
```
pip3 install -r requirements.txt
```

In case you want to implement follow the next steps:

3. Create a project on Pycharm

4. Set the venv for the project: File > Project > Project Interpreter > Show all in the dropdown menu > Choose your venv
If venv is not present: Click on '+' > Existing environment > Find the venv > Expand it > bin > choose the Python version > Ok

5. Create a Python file and have fun!

## How to run?

Run one test case or the whole suite using Chrome web browser.

- Run the suite via terminal:
Issue the below commands in project root directory
```
python -m unittest suite.py 
```

- Run specific test case via terminal:
```
 python -m unittest suite.TestLogin.TEST_NAME
```
_Example: python -m unittest suite.TestLogin.testValidLogin_

- Run test cases through IDE: 
Click on the green arrow close to the test name or in the test class.
```
python3 -m unittest testAll.TestContact.TEST_NAME
```

**Note:** The webdriver was set to run headless, if need to watch the execution, please, comment the line 12 on setUp.

## Author
<a target="_blank" href="https://github.com/diegohdb/diegohdb">👤 Diego Bezerra </a>

<a target="_blank" href="https://www.linkedin.com/in/diegohdb/">
  <img align="left" alt="LinkdeIN" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a target="_blank" href="https://www.instagram.com/diegohdb/">
  <img align="left" alt="Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a target="_blank" href="mailto:diegohdb@gmail.com">
  <img align="left" alt="Gmail" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/gmail.svg" />
</a>
