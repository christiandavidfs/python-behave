# BehavE2E

BehavE2E is a under-development testing framework/collage with the idea of being an all rounder.
Using python, webdriver for ui, allure for metrics, pandas for data processing and request for api testing, giving the verstility to be the starting point to any End to End testing project.

to install behave and allure:
sudo pip install behave
sudo pip install allure_behave


To run the tests:
behave -f allure_behave.formatter:AllureFormatter -o result
allure serve result/

To Do:

1. dockerization
2. autoupdate from repo
3. custom metrics (risk and pareto)
4. standard page objects for ui
