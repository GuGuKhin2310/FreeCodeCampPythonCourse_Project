test_settings = {
    'theme': 'light',
    'notifications': 'enabled',
    'volume': 'high'
}


def add_setting(test_settings, tuple_pair):
    key, value = tuple_pair

    key = key.lower()
    value = value.lower()

    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


print(add_setting(test_settings, ("Mode", "Dark")))


def update_setting(test_settings, tuple_pair):
    key, value = tuple_pair
    key = key.lower()
    value = value.lower()

    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


print(update_setting(test_settings, ("theme", "dark")))


def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


print(delete_setting(test_settings, ("Pick")))


def view_settings(test_settings):
    if not test_settings:
        return "No settings available."

    result = f"Current User Settings:\n"

    for key, value in test_settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result

print(view_settings(test_settings))