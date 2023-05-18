import inspect
import re
import type_converter

class orchestrator:
    def __init__(self, llm_model, function_bindings):
        self.model = llm_model
        self.function_bindings = function_bindings
        self.converter = type_converter()
        self.model.get_reply("INITIAL PROMPT!")

    def validate_description_structure(description):
        if not isinstance(description, dict):
            return False
        required_keys = ["description", "function"]
        return all(key in description for key in required_keys)

    def call_command(self, command_name, *arguments):
        target_function = None

        # Search for the target function in the list returned by return_specific_functions
        specific_functions = self.return_specific_functions(self.list_of_function_names)
        for func_dict in specific_functions:
            if func_dict["function_name"] == command_name:
                target_function = func_dict["function"]
                break

        if target_function is None:
            raise ValueError(f"Function '{command_name}' not found.")

        function_signature = inspect.signature(target_function)
        function_params = list(function_signature.parameters.values())

        if len(arguments) != len(function_params):
            raise ValueError(f"Expected {len(function_params)} arguments, but got {len(arguments)}.")

        converted_arguments = [
            self.converter.convert_type(arg, param.annotation)
            for arg, param in zip(arguments, function_params)
        ]

        response = target_function(*converted_arguments)
        return response

    def orchestrator_chat(self, prompt):
        # access the loaded llm set as orchestrator and creates an orchestrator instance, this should be used on the main function loop
        # # Print Assistant thoughts
        # print_assistant_thoughts(assistant_reply)
        reply = self.model.get_reply(prompt)

        command_pattern = re.compile(
            r'\brun (\w+)\s*\((.*)\)', flags=re.IGNORECASE)
        matches = list(re.finditer(command_pattern, reply))

        responses = []
        for match in matches:
            command_name = match.group(1)
            arguments_str = match.group(2).strip()
            if arguments_str:
                arguments = arguments_str.split(', ')
            else:
                arguments = []

            responses.append(self.call_command(command_name, *arguments))

        return reply
