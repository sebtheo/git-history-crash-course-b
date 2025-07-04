import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Access the secret from the environment variable
    secret = os.getenv("SECRET_KEY")
    
    if secret:
        print(f"The secret is: {secret}")
    else:
        print("No secret found.")
        