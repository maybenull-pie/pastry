import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"), override=True)

PIE_ENVIRONMENT = os.environ.get("PIE_ENVIRONMENT")