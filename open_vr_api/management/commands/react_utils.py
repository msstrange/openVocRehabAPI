def tuple_to_js(choice):
    return {
        'label': choice[1],
        'value': choice[0]
    }


def generate_options(choices):
    return [tuple_to_js(choice) for choice in choices]
