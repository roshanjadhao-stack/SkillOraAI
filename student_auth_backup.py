
import hashlib
import hmac
import json
import re
import secrets
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("skillora_students.db")
ITERATIONS = 600_000


def get_connection():
    connection = sqlite3.connect(str(DB_PATH), timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    connection.execute("PRAGMA busy_timeout = 10000")
    return connection


def init_auth_db():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email TEXT NOT NULL COLLATE NOCASE UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS student_progress (
                student_id INTEGER PRIMARY KEY,
                progress_json TEXT NOT NULL DEFAULT '{}',
                FOREIGN KEY(student_id)
                    REFERENCES students(id) ON DELETE CASCADE
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS student_profiles (
                student_id INTEGER PRIMARY KEY,
                phone TEXT NOT NULL DEFAULT '',
                college TEXT NOT NULL DEFAULT '',
                course TEXT NOT NULL DEFAULT '',
                skills TEXT NOT NULL DEFAULT '',
                bio TEXT NOT NULL DEFAULT '',
                location TEXT NOT NULL DEFAULT '',
                achievements TEXT NOT NULL DEFAULT '',
                photo BLOB,
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(student_id)
                    REFERENCES students(id) ON DELETE CASCADE
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS skills (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                name TEXT NOT NULL,
                level TEXT NOT NULL,
                description TEXT NOT NULL,
                project TEXT NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS learning_resources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                skill_id TEXT,
                title TEXT NOT NULL,
                resource_type TEXT NOT NULL,
                url TEXT NOT NULL DEFAULT '',
                file_path TEXT NOT NULL DEFAULT '',
                uploaded_by INTEGER,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(skill_id) REFERENCES skills(id),
                FOREIGN KEY(uploaded_by)
                    REFERENCES students(id) ON DELETE SET NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS student_skill_progress (
                student_id INTEGER NOT NULL,
                skill_id TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Not Started',
                completed_lessons INTEGER NOT NULL DEFAULT 0,
                notes TEXT NOT NULL DEFAULT '',
                updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY(student_id, skill_id),
                FOREIGN KEY(student_id)
                    REFERENCES students(id) ON DELETE CASCADE,
                FOREIGN KEY(skill_id)
                    REFERENCES skills(id) ON DELETE CASCADE
            )
        """)

        # Migrate older databases safely.
        columns = {
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(student_profiles)"
            ).fetchall()
        }

        migrations = {
            "location": "TEXT NOT NULL DEFAULT ''",
            "achievements": "TEXT NOT NULL DEFAULT ''",
            "photo": "BLOB",
        }

        for column, definition in migrations.items():
            if column not in columns:
                connection.execute(
                    f"ALTER TABLE student_profiles "
                    f"ADD COLUMN {column} {definition}"
                )


def is_valid_email(email):
    email = email.strip()
    return bool(
        re.fullmatch(
            r"[^@\s]+@[^@\s.]+(?:\.[^@\s.]+)+",
            email,
        )
    )


def _hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
    )

    return salt.hex() + "$" + password_hash.hex()


def _verify_password(password, stored_hash):
    try:
        salt_hex, hash_hex = stored_hash.split("$", 1)
        salt = bytes.fromhex(salt_hex)
        expected_hash = bytes.fromhex(hash_hex)

        actual_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            ITERATIONS,
        )

        return hmac.compare_digest(actual_hash, expected_hash)
    except (ValueError, TypeError):
        return False


def create_student(full_name, email, password):
    full_name = full_name.strip()
    email = email.strip().lower()

    if len(full_name) < 2:
        return False, "Please enter your full name."

    if not is_valid_email(email):
        return False, "Please enter a valid email address."

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    password_hash = _hash_password(password)

    try:
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO students
                    (full_name, email, password_hash)
                VALUES (?, ?, ?)
                """,
                (full_name, email, password_hash),
            )

            student_id = cursor.lastrowid

            connection.execute(
                "INSERT INTO student_progress (student_id) VALUES (?)",
                (student_id,),
            )

            connection.execute(
                "INSERT INTO student_profiles (student_id) VALUES (?)",
                (student_id,),
            )

        return True, "Account created successfully."

    except sqlite3.IntegrityError:
        return False, "This email is already registered."


def authenticate_student(email, password):
    email = email.strip().lower()

    with get_connection() as connection:
        student = connection.execute(
            """
            SELECT id, full_name, email, password_hash
            FROM students
            WHERE email = ?
            """,
            (email,),
        ).fetchone()

    if student is None:
        return None

    if not _verify_password(password, student["password_hash"]):
        return None

    return {
        "id": student["id"],
        "full_name": student["full_name"],
        "email": student["email"],
    }


def load_student_progress(student_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT progress_json
            FROM student_progress
            WHERE student_id = ?
            """,
            (student_id,),
        ).fetchone()

    if not row:
        return {}

    try:
        return json.loads(row["progress_json"])
    except (json.JSONDecodeError, TypeError):
        return {}


def save_student_progress(student_id, progress):
    progress_json = json.dumps(progress)

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO student_progress (student_id, progress_json)
            VALUES (?, ?)
            ON CONFLICT(student_id)
            DO UPDATE SET progress_json = excluded.progress_json
            """,
            (student_id, progress_json),
        )


def load_student_profile(student_id):
    with get_connection() as connection:
        row = connection.execute(
            """
            SELECT phone, college, course, skills, bio,
                   location, achievements, photo
            FROM student_profiles
            WHERE student_id = ?
            """,
            (student_id,),
        ).fetchone()

    if row is None:
        return {
            "phone": "",
            "college": "",
            "course": "",
            "skills": "",
            "bio": "",
            "location": "",
            "achievements": "",
            "photo": None,
        }

    return dict(row)


def save_student_profile(
    student_id,
    phone="",
    college="",
    course="",
    skills="",
    bio="",
    location="",
    achievements="",
    photo=None,
):
    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO student_profiles
                (student_id, phone, college, course, skills,
                 bio, location, achievements, photo, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(student_id) DO UPDATE SET
                phone = excluded.phone,
                college = excluded.college,
                course = excluded.course,
                skills = excluded.skills,
                bio = excluded.bio,
                location = excluded.location,
                achievements = excluded.achievements,
                photo = COALESCE(excluded.photo, student_profiles.photo),
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                student_id,
                phone,
                college,
                course,
                skills,
                bio,
                location,
                achievements,
                photo,
            ),
        )
