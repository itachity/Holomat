from dotenv import load_dotenv
import os

load_dotenv('sample.env')  # Must be before os.getenv(...)

my_var = os.getenv("SCREEN_WIDTH")
print("SCREEN_WIDTH:", my_var)
