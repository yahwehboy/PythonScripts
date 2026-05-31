import requests

# Replace with your Hunter.io API key
API_KEY = 'YOUR-HUNTER-API-KEY'
BASE_URL = 'https://api.hunter.io/v2'

def find_emails(domain):
    url = f"{BASE_URL}/domain-search"
    params = {
        'domain': domain,
        'api_key': API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('emails', [])
    else:
        print("Error:", response.status_code, response.text)
        return []

# Example usage
domain = 'office365.com'  # Replace with the domain you want to search
emails = find_emails(domain)

for email in emails:
    print(email['value'])  # Print out the email addresses
