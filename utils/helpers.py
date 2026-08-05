import json


def export_chat(messages):

    return json.dumps(
        messages,
        indent=4
    )



def clean_text(text):

    return text.strip()