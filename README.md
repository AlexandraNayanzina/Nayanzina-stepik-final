# Practical task for Stepik course 
Stepik course, 'Automation testing with Selenium and Python'

# Python version
Python 3.9.6

# How to run on Win
0. Prerequisites
- Python 3+
- git
- Selenium 3.14.0


1. Start Selenium
```shell
${Path_to_selenium}\Scripts\activate.bat
```
2. Create temp directory
```shell
mkdir ReviewStepikProject
cd .\ReviewStepikProject\
```
3. Clone the Project
```shell
git clone https://github.com/AlexandraNayanzina/Nayanzina-stepik-final.git
cd .\Nayanzina-stepik-final\
```
4. Run
```shell
# Test test_product_page.py
pytest -v --tb=line --language=en -m need_review test_product_page.py
```

