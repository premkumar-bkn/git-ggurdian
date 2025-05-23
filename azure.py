# example.py

# This is a fake secret (AWS Access Key) that should trigger the secret scanning tools
AZURE_SECRET_KEY = "bmH8Q~3fr73Y.wWP60kVUlZyaYUM55i5zS.YhavQ"
AZURE_CLIENT_ID = "a65f87c0-83b4-4a00-8e1b-818e1514d5dd"

def use_secrets():
    print("Using secret keys!")
    # Normally you wouldn't print these keys, but it's here for demo purposes
    print(f"Azure Client ID: {AZURE_CLIENT_ID}")
    print(f"Azure Secret Key: {AZURE_SECRET_KEY}")

if __name__ == "__main__":
    use_secrets()
