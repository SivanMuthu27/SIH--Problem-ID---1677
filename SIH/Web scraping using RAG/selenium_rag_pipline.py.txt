!apt-get update
!apt-get install -y wget unzip
!apt-get install -y chromium-browser
!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/bin/chromedriver
!pip install selenium transformers plotly