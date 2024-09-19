!apt-get update
!apt-get install -y wget unzip
!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip  # Ensure the version matches
!unzip chromedriver_linux64.zip
!mv chromedriver /usr/bin/chromedriver
!pip install selenium
!pip install transformers
!pip install plotly