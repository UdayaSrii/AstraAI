import json
import os


FILE_PATH = (
    "data/conversations.json"
)



def create_file():

    os.makedirs(
        "data",
        exist_ok=True
    )


    if not os.path.exists(FILE_PATH):

        with open(
            FILE_PATH,
            "w"
        ) as f:

            json.dump(
                {},
                f
            )



def save_conversation(
        user_id,
        messages
):


    create_file()


    with open(
        FILE_PATH,
        "r"
    ) as f:

        data=json.load(f)



    data[user_id]=messages



    with open(
        FILE_PATH,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )



def load_conversation(
        user_id
):


    create_file()


    with open(
        FILE_PATH
    ) as f:

        data=json.load(f)



    return data.get(
        user_id,
        []
    )