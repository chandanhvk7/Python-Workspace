import requests
base_url='http://172.16.10.68:1234/customers'

def get_customer():
    cid=int(input('Enter the customer id to search:'))
    r=requests.get(f'{base_url}/{cid}')
    if r.status_code==200:
        c=r.json()
        print(f'Name:{"Mr." if c["gender"]=="Male" else "Ms."}{c["firstname"]}{c["lastname"]}')
        print(f'Email:{c["email"]}')
        print(f'Phone:{c["phone"]}')
        print(f'City:{c["city"]}')
    elif r.status_code==404:
        print(f'No data found for id{cid}')
    else:
        print('Something went wrong. Please try after sometime.')

def main():
    get_customer()

if __name__=="__main__":
    main()