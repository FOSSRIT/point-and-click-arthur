import yaml
import pprint

with open("english.yaml") as stream:
    pprint.pprint(yaml.load(stream))
