import json
from pprint import pprint

def full_name(c):
    return f'{"Mr."if c["gender"]=="Male" else "Ms."}{c["first_name"]} {c["last_name"]}'

def main():
    with open('MOCK_DATA.json',encoding='utf-8') as fp:
        customers=json.load(fp)

        male_customer_names=[full_name(a_customer) for a_customer in customers if a_customer.get('gender')=='Male']
        pprint(male_customer_names)

if __name__=="__main__":
    main()