import sqlite3
import os

DB_FOLDER = os.path.join(os.path.dirname(__file__), "..", "database")
DB_FILE = os.path.join(DB_FOLDER, "toll.db")


def get_connection():
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    conn = sqlite3.connect(DB_FILE)
    return conn


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_collection (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        entry_date TEXT UNIQUE,

        shift_a_cash REAL,
        shift_a_upi REAL,

        shift_b_cash REAL,
        shift_b_upi REAL,

        shift_c_cash REAL,
        shift_c_upi REAL,

        monthly_pass REAL,

        etc_collection REAL,

        annual_single INTEGER,
        annual_return INTEGER,

        annual_amount REAL,

        total_cash REAL,

        total_upi REAL,

        total_collection REAL,

        remittance REAL,

        tcs REAL,

        upi_penalty REAL,

        upi_tcs REAL,

        total_remittance REAL,

        total_expense REAL,

        profit_loss REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        entry_date TEXT,

        description TEXT,

        amount REAL
    )
    """)

    conn.commit()
    conn.close()


def save_entry(data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO daily_collection(

    entry_date,

    shift_a_cash,
    shift_a_upi,

    shift_b_cash,
    shift_b_upi,

    shift_c_cash,
    shift_c_upi,

    monthly_pass,

    etc_collection,

    annual_single,
    annual_return,

    annual_amount,

    total_cash,

    total_upi,

    total_collection,

    remittance,

    tcs,

    upi_penalty,

    upi_tcs,

    total_remittance,

    total_expense,

    profit_loss

    )

    VALUES(

    ?,?,?,?,?,?,
    ?,?,?,?,
    ?,?,?,?,
    ?,?,?,?,
    ?,?,?,?

    )

    """, data)

    conn.commit()
    conn.close()


def save_expense(entry_date, description, amount):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO expenses(

    entry_date,
    description,
    amount

    )

    VALUES(

    ?,?,?

    )

    """, (entry_date, description, amount))

    conn.commit()
    conn.close()


def get_all():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM daily_collection ORDER BY entry_date DESC")

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_by_date(date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM daily_collection WHERE entry_date=?",

        (date,)
    )

    row = cursor.fetchone()

    conn.close()

    return row


create_table()
