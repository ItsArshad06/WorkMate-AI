from datetime import datetime

from app.database.db import get_connection


def save_session(
    telegram_user_id,
    employee_id,
    role,
    employee_name,
    department,
):
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT OR REPLACE INTO user_sessions
        (
            telegram_user_id,
            employee_id,
            role,
            employee_name,
            department,
            login_time,
            last_active
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            telegram_user_id,
            employee_id.upper(),
            role,
            employee_name,
            department,
            now,
            now,
        ),
    )

    conn.commit()
    conn.close()


def get_session(telegram_user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM user_sessions
        WHERE telegram_user_id = ?
        """,
        (telegram_user_id,),
    )

    session = cursor.fetchone()

    conn.close()

    return session


def update_last_active(telegram_user_id):
    conn = get_connection()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        UPDATE user_sessions
        SET last_active = ?
        WHERE telegram_user_id = ?
        """,
        (
            now,
            telegram_user_id,
        ),
    )

    conn.commit()
    conn.close()


def delete_session(telegram_user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM user_sessions
        WHERE telegram_user_id = ?
        """,
        (telegram_user_id,),
    )

    conn.commit()
    conn.close()