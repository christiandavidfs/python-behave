# BehavE2E

BehavE2E is a under-development testing framework/collage with the idea of being an all rounder.
Using python, webdriver for ui, allure for metrics, pandas for data processing and request for api testing, giving the verstility to be the starting point to any End to End testing project.

to install behave and allure:

sudo pip install behave

sudo pip install allure_behave

sudo apt-get install allure

sudo pip install features

sudo pip install requests

To run the tests:

behave -f allure_behave.formatter:AllureFormatter -o result


allure serve result/

To Do:

0. generate requirements.txt to install previously in venv by pip install -r requirements.txt 
1. dockerization
2. autoupdate from repo
3. custom metrics (risk and pareto)
4. standard page objects for ui
5. Enable the posibility of doing cross testing (example. hit API, database and ui visualization of the data)

Friday 4/ september roadmap next 4 weeks and requeriments to the minimal demo presentation 
