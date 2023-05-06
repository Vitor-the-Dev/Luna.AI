class orchestrator:
    def __init__(self, llm_model, service_list):
        self.llm_model = llm_model
        self.service_list = service_list
        self.function_bindings = {}


    def configparse(self, path_to_config):
    #parse config.json
        print("not implemented")

    def wrapperimport(self):
    #import all wrappers parsed on config.json]
    #binds the imported wrappers into a dict + description for different commands for the AI to use
    #pass functions imported from wrappers as keys
        for service in self.service_list:
            service_descriptions = service.get_commands()
            if service_descriptions.keys() in self.function_bindings.keys():
                continue;
            for fucntion in service_descriptions["functions"]:

                

    def call_command(self, service_name, command_name, arguments**):
        if command_name in self.service_list:
            self.service_list[service_name][command_name]["function"](arguments)
        else:
            print("Command not found")

    def orchestrator_chat(self, prompt):
    #access the loaded llm set as orchestrator and creates an orchestrator instance, this should be used on the main function loop
        # with Spinner("Thinking... "):
        # assistant_reply = chat.chat_with_ai(
        #     prompt,
        #     user_input,
        #     full_message_history,
        #     memory,
        #     cfg.fast_token_limit) # TODO: This hardcodes the model to use GPT3.5. Make this an argument

        # # Print Assistant thoughts
        # print_assistant_thoughts(assistant_reply)
        reply = self.model.get_reply(prompt)



    



