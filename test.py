import json

print("test")

with open("metrics.json", "w") as f:
	json.dump({"accuracy": 0.98, "evaluation_samples": 1000}, f)