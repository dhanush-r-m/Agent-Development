from .agent import root_agent

# ADK expects greeting_agent.agent.root_agent
class AgentWrapper:
    root_agent = root_agent

agent = AgentWrapper()
