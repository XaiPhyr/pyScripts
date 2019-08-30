import os
import argparse

parser = argparse.ArgumentParser(description='Incognito ready...', version='0.0.1.a')
parser.add_argument('site', help='redirect to website.')

args = parser.parse_args()

if args.site:
    site = args.site
    os.system('chromium --incognito ' + site)
else:
    print('Site: ' + args.site)