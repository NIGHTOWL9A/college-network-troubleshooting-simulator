import json

def load_scenarios():
    with open("scenarios/scenarios.json", encoding="utf-8") as f:
        return json.load(f)

def run():
    scenarios = load_scenarios()
    score = 0
    print("\nCollege Network Troubleshooting Simulator")
    print("=" * 45)
    for i, s in enumerate(scenarios, 1):
        print(f"\nScenario {i}: {s['title']}")
        print(s["description"])
        for j, option in enumerate(s["options"], 1):
            print(f"{j}. {option}")
        while True:
            try:
                choice = int(input("Choose the most likely cause: "))
                if 1 <= choice <= len(s["options"]):
                    break
            except ValueError:
                pass
            print("Enter a valid option.")
        if choice == s["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. Correct answer: {s['options'][s['answer'] - 1]}")
        print("Explanation:", s["explanation"])
    print(f"\nFinal Score: {score}/{len(scenarios)}")

if __name__ == "__main__":
    run()
