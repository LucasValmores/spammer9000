import requests
import threading

# Define the URL of the scammer (or a testing endpoint like httpbin)
url = '[INSERTURL]'

# Function to generate fake data
def generate_fake_data():
    return {
        'USER': "",
        'PASS': "",
        'CATEGORY': "",
        'CONTINENT': "",
        'COUNTRY': "",
        'CAPITAL': "",
        'STATE': "",
        'CITY': "",
        'CURRENCY': "",
        'PHONE_CODE': "",
        'IP_ADDRESS': ""


    }

# Function to send fake data
def send_fake_data(url, data):
    try:
        response = requests.post(url, data=data)
        print(f'Status Code: {response.status_code}, Response: {response.text}')

    except Exception as e:
        print(f'An error occurred: {e}')



def kill():
    while True:
        fake_data = generate_fake_data()
        send_fake_data(url, fake_data)
        print("[CONFIRM MESSAGE]")




threads = []


for i in range(100):
    t = threading.Thread(target=kill)
    t.daemon = True
    threads.append(t)

for i in range (100):
    threads[i].start()

for i in range (100):
    threads[i].join()


