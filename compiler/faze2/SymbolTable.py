class SymbolTable:
    def __init__(
        self,
        name,
        var_type,
        is_function,
        is_argumman,
        is_array,
        num_params,
        is_assigned_value=False,
        is_defined_symbol=True,
    ):
        self.name = name
        self.var_type = var_type
        self.is_function = is_function
        self.is_argumman = is_argumman
        self.is_array = is_array
        self.num_params = num_params
        self.is_assigned_value = is_assigned_value
        self.is_defined_symbol = is_defined_symbol
        self.param_list = []
        self.param_type_list = []
        self.value = None

    def add_parameter(self, arguman_name):
        self.param_list.append(arguman_name)

    def add_parameter_type(self, arguman_type):
        self.param_type_list.append(arguman_type)

    def get_parameter(self):
        return [p for p in self.param_list]

    def get_parameter_typesss(self):
        return [p for p in self.param_type_list]

    def get_names(self):
        return [p for p in self.name]

    def assign_value(self, value):
        if self.is_assigned_value == True:
            self.value = value

    def __str__(self):
        if self.is_function:
            return f"function_identifire: {self.name}\nargummans:({', '.join(self.param_list)})"
        else:
            return self.name
