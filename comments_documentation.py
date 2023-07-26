# Good practice (Function with docstring)
def greet(name):
    """
    Greets the user with the given name.

    Parameters:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

# Avoid (No comments)
def greet(name):
    return f"Hello, {name}!"
