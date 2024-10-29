import os #for operation system interactions
import time #for current time that logged 
import requests #for API requests
import logging #for log and monitor

# Environment variables for configuration
HERCULES_URL = os.getenv("HERCULES_URL", "http://hercules") #change it to your IP/DNS
HERCULES_PORT = os.getenv("HERCULES_PORT", "80")  # Change to the port number you want
LOG_FILE = os.getenv("LOG_FILE", "/var/log/hercules_health.log")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60")) #Change it to the time that you want to monitor
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper() #Can change it to INFO, DEBUG, WARNING and ERROR

def configure_logging():
    """
    Configures the logging settings for the application to output to both file and stdout.
    Log level is set based on the LOG_LEVEL environment variable.
    """
    level_info = getattr(logging, LOG_LEVEL, logging.INFO)  # Change the default to INFO if LOG_LEVEL is invalid
    logging.basicConfig(
        level=level_info,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging configured. Writing logs to %s with level %s", LOG_FILE, LOG_LEVEL)

def check_hercules_health():
    """
    Performs a health check on the Hercules Nginx service by making a GET request.
    Logs the status based on the HTTP response or connection error.
    """
    url = f"{HERCULES_URL}:{HERCULES_PORT}"
    try:
        response = requests.get(url)
        if response.status_code == 200: #If Rest API returns with 20 code mean that we are good
            logging.info(f"Hercules is up - Status: {response.status_code}")
        else:
            logging.warning(f"Hercules returned unexpected status - Status: {response.status_code}")
    except requests.ConnectionError:
        logging.error("Hercules is down - Connection Error")

def main_loop():
    """
    Main loop function that periodically checks the Hercules service health.
    Runs indefinitely with a specified interval between checks.
    """
    logging.info("Starting Hercules health check service with URL %s", HERCULES_URL)
    logging.info("Check interval set to %s seconds", CHECK_INTERVAL)
    
    while True: #Runs without stopping in loop
        check_hercules_health()
        logging.info("Waiting %s seconds before the next check.", CHECK_INTERVAL)
        time.sleep(CHECK_INTERVAL)

#main function that calls to the other functions
if __name__ == "__main__":
    configure_logging()
    main_loop()
