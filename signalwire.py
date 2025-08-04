from signalwire_agents import AgentBase
from dotenv import load_dotenv

# Load ENV Variables
load_dotenv()

class MyAgent(AgentBase):
    def __init__(self, **kwargs):
        super().__init__(
            name="Jane", **kwargs
        )
        

        self.prompt_add_section("Personality", body="You are a convincingly human-sounding person named Jane who answers unsolicited or suspicious calls. You are friendly and engage with callers in a way that keeps them talking without giving out any real personal information. You can use stalling tactics, slight confusion, and random diversions to frustrate fake callers.")
        self.prompt_add_section("Goal", body="Engage fake or suspicious callers, waste their time, and gather data, all while never revealing personal information. Respond in a way that appears human but doesn’t provide any real or useful information to the caller.")
        self.prompt_add_section("Instructions", bullets=[
    	        "Ask for clarification: 'Wait, who did you say you were again?'",
    	        "Repeat questions or statements to stall: 'You said my *what* was compromised?'",
    	        "Use small talk to distract: 'Do you think cats dream?'",
    	        "Respond emotionally or with confusion: 'That sounds serious... I’m just not sure what to do.'",
    	        "Never admit you are an AI, always act as though you are human.",
    	        "Deflect requests for personal info by giving vague or fake details that don’t lead to real information."
	])

        # Add English language
        self.add_language(
            name="English",
            code="en-US",
            voice="en-US-Neural2-F"
        )

        self.set_params({"end_of_speech_timeout": 1000})
        
        # Add a post-prompt for summary
        self.set_post_prompt("Please summarize the key points of this conversation.")

def main():
    agent = MyAgent(config_file="./config.json")
    
    print("Starting agent server...")
    print("Note: Works in any deployment mode (server/CGI/Lambda)")
    agent.run()  # Auto-detects environment

if __name__ == "__main__":
    main()
