import sqlite3
from datetime import datetime
from typing import List, Dict

DB_PATH = "src/database/totem.db"


def _get_conn():
    return sqlite3.connect(DB_PATH)


def init_db() -> None:
    conn = _get_conn()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_type TEXT NOT NULL,
            value REAL NOT NULL,
            prediction TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def save_interaction(valor: float, pred: str, sensor_type: str = "sensor_simulado") -> None:
    init_db()
    conn = _get_conn()
    cursor = conn.cursor()

    created_at = datetime.now().replace(microsecond=0).isoformat()

    cursor.execute(
        """
        INSERT INTO interactions (sensor_type, value, prediction, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (sensor_type, float(valor), str(pred), created_at),
    )

    conn.commit()
    conn.close()


def get_interactions(limit: int = 50) -> List[Dict]:
    init_db()
    conn = _get_conn()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, sensor_type, value, prediction, created_at
        FROM interactions
        ORDER BY id DESC
        LIMIT ?
        """,
        (int(limit),),
    )

    rows = cursor.fetchall()
    conn.close()

    return [dict(r) for r in rows]