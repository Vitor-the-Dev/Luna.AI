import re


class orchestrator:
    def __init__(self, llm_model, service_list):
        self.llm_model = llm_model
        self.service_list = service_list
        self.function_bindings = {}
        self.wrapperimport()

    def validate_description_structure(description):
        if not isinstance(description, dict):
            return False
        required_keys = ["description", "function"]
        return all(key in description for key in required_keys)

    def wrapperimport(self):
        # import all wrappers parsed on config.json]
        # binds the imported wrappers into a dict + description for different commands for the AI to use
        # pass functions imported from wrappers as keys

        for obj in self.service_list:
            all_command_names = set()
            if hasattr(obj, "get_command_descriptions"):
                service_name, commands = obj.get_command_descriptions()

                if service_name in self.function_bindings:
                    continue

                for command_name, command_info in commands.items():
                    if not self.validate_description_structure(command_info):
                        continue

                    if command_name in all_command_names:
                        continue

                    all_command_names.add(command_name)

                self.function_bindings[service_name] = commands

    def call_command(self, service_name, command_name, *arguments):
        if command_name in self.function_bindings[service_name]:
            self.service_list[service_name][command_name]["function"](
                *arguments)
            return True
        else:
            return False

    def orchestrator_chat(self, prompt):
        # access the loaded llm set as orchestrator and creates an orchestrator instance, this should be used on the main function loop
        # # Print Assistant thoughts
        # print_assistant_thoughts(assistant_reply)
        reply = self.model.get_reply(prompt)
        command_pattern = re.compile(
            r'\brun (\w+) (\w+)(.*)', flags=re.IGNORECASE)
        matches = list(re.finditer(command_pattern, reply))

        responses = []
        for match in matches:
            service_name = match.group(1)
            command_name = match.group(2)
            arguments = match.group(3).strip().split()
            self.call_command(service_name, command_name, *arguments)

        return (reply)
