# BehavE2E

BehavE2E is a under-development testing framework/collage with the idea of being an all rounder.
Using python, appium for ui, allure for metrics, pandas for data processing and request for api testing, giving the verstility to be the starting point to any End to End testing project.

to install behave and allure:

sudo pip install behave

sudo pip install allure_behave

sudo apt-get install allure

sudo pip install features

sudo pip install requests

To run the tests:

behave -f allure_behave.formatter:AllureFormatter -o result


allure serve result/ -> add route for debian
or validate allure route: whereis allure and use the displayed route

To Do:

0. generate requirements.txt to install previously in venv by pip install -r requirements.txt 
1. dockerization (80% finished, lacking some tests and alternatives realeted to db persistance)
2. autoupdate from repo (two methods working, still deciding wich one is better)
3. custom metrics (risk and pareto)
4. standard page objects for ui 
5. Enable the posibility of doing cross testing (example. hit API, database and ui visualization of the data)
6. Integration with Browserstack (Thanks for the 1 year Sponsorship)
7. Secret manager
8. Sikuli vs OpenCV

Friday 4/ september roadmap next 4 weeks and requeriments to the minimal demo presentation 

Done:

0. A unique json is generated and managed to connect to postgres database to upload the data generated by allure. Still needed to create the database 
1. API testing in BDD (lacking tests winth connections with tokens or auth)

Reimplementations:

0. Migration from postgres to MongoDB (finished) still learning to do the visualizations.
