def after5(original_function):
    def new_function():
        original_function()

    return new_function
