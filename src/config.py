import os

"""
Ini adalah file untuk mengatur konfigurasi seluruh script
"""


# Cascade file configuration
CASCADE_ROOT = 'CascadeFile'
FACE_CASCADE = 'face-detect.xml'
FACE_CASCADE_PTH = os.path.join(CASCADE_ROOT, FACE_CASCADE)

# Recognizer configuration
MODEL_ROOT = 'model'
MODEL_NAME = 'recognizer.yml'
MODEL_PTH = os.path.join(MODEL_ROOT, MODEL_NAME)
THRESHOLD = 70

# Data configuration
DATA_ROOT = 'data'
TOTAL_DATA = 10

# DB Configuration
DB_ROOT = 'database'
DB_NAME = 'database.db'
DB_PATH = os.path.join(DB_ROOT, DB_NAME)

CREATE_TABLE_QUERY = """CREATE TABLE IF NOT EXISTS Data (
                            id integer NOT NULL,
                            name text NOT NULL
                        );"""

SHOW_QUERY = """SELECT * FROM Data"""


INSERT_DATA_QUERY = """INSERT INTO Data (id, name) VALUES (?, ?)"""

UPDATE_DATA_QUERY = """UPDATE Data
                       SET name = ?
                       WHERE id = ?
                    """

SELECT_NAME_QUERY = """SELECT name
                       FROM Data 
                       WHERE id = ?
                    """
DELETE_DATA_QUERY = """DELETE FROM Data WHERE id = ?"""
