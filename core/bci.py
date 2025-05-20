class ThoughtToText:
    def __init__(self):
        self.history = []

    def capture_thought(self, simulated_thought):
        print(f"BCI: Translating your thought – '{simulated_thought}'")
        self.history.append(simulated_thought)
        self.log_thought(simulated_thought)

    def log_thought(self, thought):
        with open("logs/thought_log.txt", "a") as f:
            f.write(f"{thought}\n")
        print("BCI: Thought logged successfully.")
