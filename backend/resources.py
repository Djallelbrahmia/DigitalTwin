import json



with open("./data/me.txt", "r", encoding="utf-8") as f:
    summary = f.read()

with open("./data/styles.txt", "r", encoding="utf-8") as f:
    style = f.read()

with open("./data/facts.json", "r", encoding="utf-8") as f:
    facts = json.load(f)