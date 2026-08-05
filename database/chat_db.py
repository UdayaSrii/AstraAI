import sqlite3
import os
from datetime import datetime


DB_PATH = "data/persona_ai.db"


def create_database():

    os.makedirs(
        "data",
        exist_ok=True
    )

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chats
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            title TEXT,
            created_at TEXT
        )
        """
    )


    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS messages
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            role TEXT,
            content TEXT,
            created_at TEXT
        )
        """
    )


    connection.commit()

    connection.close()



def create_chat(
        user,
        title
):

    create_database()

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO chats
        (
            user,
            title,
            created_at
        )
        VALUES (?, ?, ?)
        """,
        (
            user,
            title,
            datetime.now().isoformat()
        )
    )


    chat_id = cursor.lastrowid


    connection.commit()

    connection.close()


    return chat_id



def save_message(
        chat_id,
        role,
        content
):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO messages
        (
            chat_id,
            role,
            content,
            created_at
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            chat_id,
            role,
            content,
            datetime.now().isoformat()
        )
    )


    connection.commit()

    connection.close()



def get_messages(
        chat_id
):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT role, content
        FROM messages
        WHERE chat_id=?
        """,
        (
            chat_id,
        )
    )


    rows = cursor.fetchall()


    connection.close()


    return [

        {
            "role": row[0],
            "content": row[1]
        }

        for row in rows

    ]



def get_user_chats(
        user
):

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT id,title
        FROM chats
        WHERE user=?
        ORDER BY id DESC
        """,
        (
            user,
        )
    )


    chats = cursor.fetchall()


    connection.close()


    return chats