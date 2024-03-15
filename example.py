from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

with open("securityevent.schema.json", "r") as f:
    schema = json.load(f)

with open("sample.json", "r") as f:
    sample = json.load(f)
try:

    validate(instance=sample, schema=schema)

except ValidationError as e:
    print(e)
