import argparse
import json
from pprint import pprint

def main():
    parser=argparse.ArgumentParser(description='Produces a filtered content from the input json file')
    parser.add_argument('-f','--filename',help='input json Filename',required=True)
    parser.add_argument('-p','--property',help='property to check',required=True)
    parser.add_argument('-v','--value',help='value of the property to check',required=True)
    parser.add_argument('-o','--outfile',help='output json Filename')
    args=parser.parse_args()
    with open(args.filename,encoding='utf-8',mode='rt') as fp:
        data=json.load(fp)
        output_data=[each_data for each_data in data if each_data.get(args.property)==args.value]
    if args.outfile is None:
        pprint(output_data)
    else:
        with open(args.outfile, mode='wt') as fp:
            json.dump(output_data,fp)
            print(f'{len(output_data)} objects added to file "{args.outfile}"')




if __name__=="__main__":
    main()

    