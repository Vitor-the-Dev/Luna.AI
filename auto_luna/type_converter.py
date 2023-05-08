import ast

class type_coverter:
    
    def __init__(self):
        self.config = {}
    
    def convert_type(self, s, target_type):
        if target_type == int:
            return int(s)
        elif target_type == float:
            return float(s)
        elif target_type == bool:
            return s.lower() in ['true', '1']
        elif target_type == str:
            return s
        else:
            try:
                literal_value = ast.literal_eval(s)
                if isinstance(literal_value, target_type):
                    return literal_value
                else:
                    raise ValueError(f"Value '{s}' cannot be converted to the target type '{target_type}'.")
            except ValueError:
                raise ValueError(f"Conversion to type '{target_type}' not supported or invalid input.")