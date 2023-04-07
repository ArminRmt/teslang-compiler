class SymbolTable:
    def __init__(
        self,
        name,
        var_type,
        is_function,
        is_argumman,
        num_params,
        is_assigned_value=False,
        is_defined_symbol=True,
    ):
        self.name = name
        self.var_type = var_type
        self.is_function = is_function
        self.is_argumman = is_argumman
        self.num_params = num_params
        self.is_assigned_value = is_assigned_value
        self.is_defined_symbol = is_defined_symbol
        self.param_list = []
        self.value = None

    def add_parameter(self, name):
        self.param_list.append(name)

    def get_parameter_types(self):
        return [p[0] for p in self.param_list]

    def get_names(self):
        return [p for p in self.name]

    def assign_value(self, value):
        if self.is_assigned_value == True:
            self.value = value

    def __str__(self):
        return f"{self.name}: {'function_identifire' if self.is_function else 'varible_identifire'}"
