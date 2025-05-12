# example.py

# This is a fake secret (AWS Access Key) that should trigger the secret scanning tools
AWS_SECRET_ACCESS_KEY = "AKIAEXAMPLESECRET12345"
AWS_ACCESS_KEY_ID = "AKIAEXAMPLEACCESSKEY12345"

def use_secrets():
    print("Using secret keys!")
    # Normally you wouldn't print these keys, but it's here for demo purposes
    print(f"AWS Access Key ID: {AWS_ACCESS_KEY_ID}")
    print(f"AWS Secret Access Key: {AWS_SECRET_ACCESS_KEY}")

if __name__ == "__main__":
    use_secrets()
