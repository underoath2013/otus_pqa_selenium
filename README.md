# otus_pqa_selenium
docker build . -t tests-opencart  
docker run --rm tests-opencart

docker-compose up --build  
docker-compose down

docker network ls  
docker network inspect selenoid

allure generate allure-results -c  
allure open .\allure-report\

.\cm.exe selenoid start --vnc  
.\cm.exe selenoid stop  
pytest -n 2 --remote  
pytest -n 2 --remote --bv 115.0  
pytest -n 4 --remote --bv 114.0  

