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

    def get_luna_functions(self):

        return {"wrapper name":"agent_manager","functions":[{"name":"create_agent", "description":"parameters: task - the task the agent is meant to perform, prompt - the initial prompt or the message to the agent, model - the LLM to be used; description: The function first creates an empty list with the user's initial prompt. Then it calls 'create_chat_completion' function to generate the chatbot's initial response based on the prompt and selected model. The resulting response is appended to the messages list along with the role of the assistant. A unique key is generated for the new agent by incrementing the 'next_key' attribute. The new agent is then added to the 'agents' dictionary, which maps keys to tuples containing the task, message history, and LLM for each agent.; return: the method returns the key of the new agent and the initial response generated by the LLM.","function":self.create_agent()}, {"name":"message_agent", "description":"parameters: key - unique key allowing the user to send a specified message to a previously created AI chatbot, message - a user written prompt for the LLM agent; description: The function retrieves the chatbot's current converstation history, adds the new message to the history and then uses the GPT-3 API to generate a response to the message. Finally the generated response is appended to the converstation history.; return: the generated response is returned as a string","function":self.message_agent()}, {"name":"list_agents", "description":"parameters: ; description: The 'list_agents' method returns a list of tuples where each tuple contains two elements, the key assigned to the agent and its associated task. The key is the unique identifier assigned to the agent and the value is a tuple that contains the agent's task, message history and LLM.; return: the list is returned","function":self.list_agents()}, {"name":"delete_agent", "description":"parameters: ; description: ; return:","function":self.delete_agent()}]}