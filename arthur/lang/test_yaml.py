import yaml
import pprint

with open("english.yaml") as stream:
    d = yaml.load(stream)

for dialog_object in  d['PLACES']['shack']['ACTIONS']['first_visit']['DIALOG']:
    for blurb in dialog_object["TEXT"]:
        print "%s says '%s'" % (dialog_object['ACTOR'], blurb)
