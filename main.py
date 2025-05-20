from core.neuro_modes import CognitiveModes
from core.assistant import NeuroAI
from core.bci import ThoughtToText
from ui.app import launch_ui

def run_neurolink_os():
    print("Welcome to NeuroLinkOS – The AI Operating System for the Human Mind")
    
    # Initialize modules
    modes = CognitiveModes()
    assistant = NeuroAI()
    bci = ThoughtToText()

    # Simulate user experience
    modes.activate_mode("focus")
    assistant.respond("What should I do today?")
    bci.capture_thought("Build my future with AI")

    # Launch UI (optional in CLI)
    launch_ui()

if __name__ == "__main__":
    run_neurolink_os()
