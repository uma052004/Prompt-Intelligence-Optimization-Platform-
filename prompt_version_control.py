import json
import os
from datetime import datetime

FILE_NAME = "prompt_versions.json"


def load_versions():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_versions(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_prompt_version(original_prompt, new_prompt, total_score, explainability):
    data = load_versions()

    # Find existing prompt record
    for record in data:
        if record["original_prompt"] == original_prompt:
            version_no = len(record["versions"]) + 1
            record["versions"].append({
                "version": version_no,
                "prompt": new_prompt,
                "total_score": total_score,
                "explainability": explainability,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            save_versions(data)
            return

    # New prompt record
    data.append({
        "original_prompt": original_prompt,
        "versions": [{
            "version": 1,
            "prompt": new_prompt,
            "total_score": total_score,
            "explainability": explainability,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]
    })

    save_versions(data)
