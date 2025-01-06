import json

# File paths
input_file = "intents.json"
output_file = "intents_cleaned.json"


def clean_intents(file_path, output_path):
    # Load the JSON file
    with open(file_path, "r") as file:
        intents = json.load(file)

    # Cleaned intents list
    cleaned_intents = []

    for intent in intents:
        # Skip intents missing required keys
        if not all(key in intent for key in ["tag", "patterns", "responses"]):
            print(f"Skipping invalid intent: {intent}")
            continue

        # Remove duplicates and empty patterns/responses
        tag = intent["tag"]
        patterns = list(set(filter(None, intent["patterns"])))  # Remove duplicates and empty patterns
        responses = list(set(filter(None, intent["responses"])))  # Remove duplicates and empty responses

        # Skip intents with empty patterns or responses
        if not patterns or not responses:
            print(f"Skipping intent with empty patterns/responses: {tag}")
            continue

        # Append cleaned intent
        cleaned_intents.append({
            "tag": tag,
            "patterns": patterns,
            "responses": responses
        })

    # Save cleaned intents to a new file
    with open(output_path, "w") as file:
        json.dump(cleaned_intents, file, indent=4)

    print(f"Cleaned intents saved to {output_path}")


# Run the cleaning function
clean_intents(input_file, output_file)
