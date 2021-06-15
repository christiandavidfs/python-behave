behave -f allure_behave.formatter:AllureFormatter -o result/
read -t 5 -p "Starting Allure Server ..."
allure serve result/
