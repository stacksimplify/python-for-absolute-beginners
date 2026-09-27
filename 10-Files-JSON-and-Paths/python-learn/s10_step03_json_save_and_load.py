# JSON is the everyday format for saving structured data, like settings or a record.
# Concept-01: json.dumps -> a dict to a JSON STRING; json.loads -> the string back to a dict (the s = string)
# Question: How do we turn a dict into JSON text we can print, send or log, and turn that text back into a dict?
import json

person = {"name": "Kalyan", "age": 30, "languages": ["Python", "Bash"]}
text = json.dumps(person)   # dict -> a JSON string (not a file)
print(text)
print(type(text))

back = json.loads(text)     # JSON string -> a dict again
print("first language is:", back["languages"][0])

# Concept-02: json.dump is that same JSON written straight into a FILE; no s means a file (indent=2 makes it easy to read)
# Question: How do we save a Python dictionary {"name": "Kalyan", "age": 30, "languages": ["Python", "Bash"]} with strings, numbers, and lists to a file so we can read it back later?
import json

# A dictionary with a few different value types.
person = {"name": "Kalyan", "age": 30, "languages": ["Python", "Bash"]}
with open("demo_data.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2)

# Read the file back as plain TEXT (mode "r" from Step-01) to SEE what indent=2 wrote.
with open("demo_data.json", "r", encoding="utf-8") as f:
    print(f.read())

# Concept-03: json.load reads that file back into a normal Python dict
# Question: How do we read a JSON file (demo_data.json) back into a Python dictionary with all the original types and structure?
import json
from pathlib import Path

# The same file as Concept-02, saved again so this block stands on its own
person = {"name": "Kalyan", "age": 30, "languages": ["Python", "Bash"]}
with open("demo_data.json", "w", encoding="utf-8") as f:
    json.dump(person, f, indent=2)

with open("demo_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
print("name is:", loaded["name"])
print("first language is:", loaded["languages"][0])

# Remove file created
Path("demo_data.json").unlink()
