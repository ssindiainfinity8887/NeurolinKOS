class CognitiveModes:
    def __init__(self):
        self.modes = {
            "focus": self.focus_mode,
            "creative": self.creative_mode,
            "relax": self.relax_mode
        }

    def activate_mode(self, mode_name):
        mode = self.modes.get(mode_name.lower())
        if mode:
            print(f"Activating {mode_name.capitalize()} Mode...")
            mode()
        else:
            print("Mode not found. Available modes: focus, creative, relax")

    def focus_mode(self):
        print("Distraction blockers enabled. Let's get to work!")

    def creative_mode(self):
        print("Mind maps activated. Imagination unleashed!")

    def relax_mode(self):
        print("Starting guided meditation and emotional check-in.")
