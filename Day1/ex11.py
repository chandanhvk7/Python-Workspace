#DICTIONARy

from pprint import pprint #pretty print
import json

def main():
    p1=dict(name='Chandan',email='chand@n.com',married=False)
    p1['address']=dict(city='Shivamogga',state='Karnataka')
    p1['phones']=['7204042026','9731424784']

    del p1['email'] #p1.pop('email')

    pprint(p1)
    print('_'*50)
    print(json.dumps(p1,indent=4))
    print(p1.keys())
    print(p1.values())
    print(p1.items())
    
    print(f'p1["name"] is {p1["name"]}')
    #print(f'p1["gender"] is {p1["gender"]}') would result in KeyError
    print(f'p1.get("gender") is {p1.get("gender","male")}')

    if 'email' in p1:
        print(f'p1 has an email and it is {p1["email"]}')

if __name__=="__main__":
    main()