CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users 
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE(TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?)
"""

CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile 
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKAME CHAR(50),
BIO TEXT,
PHOTO TEXT,
UNIQUE(TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES(?,?,?,?,?)
"""

SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""

CREATE_LIKE_DISLIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_dislike 
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
LIKE_STATUS INTEGER,
UNIQUE(OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_dislike VALUES(?,?,?,?)
"""

SELECT_ALL_PROFILES = """
SELECT * FROM profile p 
WHERE p.TELEGRAM_ID NOT IN (
    SELECT ld.OWNER_TELEGRAM_ID
    FROM like_dislike ld
    WHERE ld.LIKER_TELEGRAM_ID = ?
    AND ld.LIKE_STATUS IS NOT NULL
)
AND p.TELEGRAM_ID != ?
"""
