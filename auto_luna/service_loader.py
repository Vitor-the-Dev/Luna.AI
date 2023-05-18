class service_loader:
    def __init__(self):
        self.list_of_classes = []
        self.list_of_modules = []

    def return_all_function_descriptions(self):
        list_of_descriptions = []
        new_list = []
        for i in self.list_of_classes:
            new_list.extend(i.function_descriptions()["functions"])
        for i in self.list_of_modules:
            new_list.extend(i.function_descriptions()["functions"])
        for i in new_list.extend(self.list_of_modules, self.list_of_classes):
            list_of_descriptions.append({"name":i["function_name"], "description":i["function_description"]})
        return list_of_descriptions
    
    def return_specific_functions(self, list_of_function_names):
        final_function_list = []
        class_instances = {}

        for func_name in list_of_function_names:
            found = False
            
            # Search in list_of_classes
            for cls_dict in self.list_of_classes:
                cls = cls_dict["class"]
                if cls not in class_instances:
                    class_instances[cls] = cls()
                
                functions = cls.function_description()["functions"]
                for func in functions:
                    if func["function_name"] == func_name:
                        modified_func = func.copy()
                        modified_func["function_name"] = f'{cls_dict["service_name"]}.{func_name}'
                        final_function_list.append(modified_func)
                        found = True
                        break

                if found:
                    break

            if not found:
                # Search in list_of_modules
                for module_dict in self.list_of_modules:
                    module = module_dict["module"]
                    functions = module.function_description()["functions"]
                    for func in functions:
                        if func["function_name"] == func_name:
                            modified_func = func.copy()
                            modified_func["function_name"] = f'{module_dict["service_name"]}.{func_name}'
                            final_function_list.append(modified_func)
                            found = True
                            break

                    if found:
                        break

        return final_function_list