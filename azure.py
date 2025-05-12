# example.py

# This is a fake secret (AWS Access Key) that should trigger the secret scanning tools
# AZURE_SECRET_KEY = "bmH8Q~3fr73Y.wWP60kVUlZyaYUM55i5zS.YhavQ"
# AZURE_CLIENT_ID = "a65f87c0-83b4-4a00-8e1b-818e1514d5dd"

# AZURE_CLIENT_ID="a65f87c0-83b4-4a00-8e1b-818e1514d5dd"
# AZURE_CLIENT_SECRET="bmH8Q~3fr73Y.wWP60kVUlZyaYUM55i5zS.YhavQ"
# AZURE_TENANT_ID="dafc6bf4-f880-4a18-b6f6-612be4218e5f"
# AZURE_SUBSCRIPTION_ID="e8d19c40-8211-40d2-985f-800fd1402b70"

def use_secrets():
    print("Using secret keys!")
    # Normally you wouldn't print these keys, but it's here for demo purposes
    print(f"Azure Client ID: {AZURE_CLIENT_ID}")
    print(f"Azure Secret Key: {AZURE_SECRET_KEY}")

if __name__ == "__main__":
    use_secrets()
