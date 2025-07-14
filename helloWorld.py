from typing import TypedDict

# Define a dictionary structure with one key: 'message'
class AgentState(TypedDict):
    message : str

# Define a function that takes AgentState and returns AgentState
def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting to the message"""
    state['message'] = "Hey " + state["message"] + ", how was your day going"
    return state



print(output_state)
# Output: {'message': 'Hey Pratik, how was your day going'}
