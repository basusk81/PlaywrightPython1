import os
#from dotenv import load_dotenv

#load_dotenv()

class Config:
    OIC_API_BASE_URL = os.getenv("OIC_API_BASE_URL")
    API_TOKEN = os.getenv("API_TOKEN")
    