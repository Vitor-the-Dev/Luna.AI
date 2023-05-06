from llm_utils import create_chat_completion

class agent_manager:

    def __init__(self, next_key=0, agents={}):    
        self.next_key = next_key
        self.agents = {}  # key, (task, full_message_history, model)

    # Create new GPT agent
    # TODO: Centralise use of create_chat_completion() to globally enforce token limit

    def create_agent(self, task, prompt, model):

        messages = [{"role": "user", "content": prompt}, ]

        # Start GTP3 instance
        agent_reply = create_chat_completion(
            model=model,
            messages=messages,
        )

        # Update full message history
        messages.append({"role": "assistant", "content": agent_reply})

        key = self.next_key
        # This is done instead of len(agents) to make keys unique even if agents
        # are deleted
        self.next_key += 1

        self.agents[key] = (task, messages, model)

        return key, agent_reply


    def message_agent(self, key, message):

        task, messages, model = self.agents[int(key)]

        # Add user message to message history before sending to agent
        messages.append({"role": "user", "content": message})

        # Start GTP3 instance
        agent_reply = create_chat_completion(
            model=model,
            messages=messages,
        )

        # Update full message history
        messages.append({"role": "assistant", "content": agent_reply})

        return agent_reply


    def list_agents(self):

        # Return a list of agent keys and their tasks
        return [(key, task) for key, (task, _, _) in self.agents.items()]


    def delete_agent(self, key):

        try:
            del self.agents[int(key)]
            return True
        except KeyError:
            return False