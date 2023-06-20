from jsonschema import validate
import json

with open("securityevent.schema.json", "r") as f:
    schema = json.load(f)

with open("sample.json", "r") as f:
    sample = json.load(f)

validate(instance=sample, schema=schema)
