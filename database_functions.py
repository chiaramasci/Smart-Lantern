"""
database_functions.py


"""
import sqlite3

DATABASE_NAME = 'database.db'

def open_connection():
    return sqlite3.connect(DATABASE_NAME)

def get_next_direction(position_now):
    """
    It gets from the table PATH the next direction

    Args:
        position_now(int): the present position

    Returns:
        direction

    Raise:
        ValueError
    """
    conn = open_connection()
    cursor = conn.execute('SELECT * FROM PATH WHERE POSITION = %d' %position_now)
    if len(cursor.fetchall()) > 1 or len(cursor.fetchall()) == 0:
        raise ValueError('Error in the table PATH: len(cursor) = ',len(cursor.fetchall()))
    else:
        row = cursor.fetchall()
        direction = row[0][1]
        return direction

    conn.close()

def create_record(numcard,username,position,direction):
    """
    Create new row in DATA table

    Args:
        numcard(string)
        username(string)
        position(int)
        direction(string)
    """

    conn = open_connection()
    cursor = conn.execute('SELECT ncard,username,position,direction FROM DATA WHERE ncard = "%s"' %(numcard))
    if len(cursor.fetchall()) == 0:
        conn.execute('INSERT INTO DATA VALUES ("%s","%s",%d,"%s")' %(numcard,username,position,direction))
    else:
        conn.execute('UPDATE DATA SET POSITION = %d, DIRECTION = "%s" WHERE NCARD = "%s"' %(position,direction,numcard))
    conn.commit()
    conn.close()

def update_record(numcard,position,direction):
    """
    updates the position and the direction in the row of numcard

    Args:
        numcard(string)
        position(int)
        direction(string)

    """

    conn = open_connection()
    conn.execute("UPDATE DATA SET POSITION = %d, DIRECTION = '%s' WHERE NCARD = '%s' " %(position,direction,numcard))
    conn.commit()
    conn.close()

def get_direction_raspberry(numcard):
    """
    function to get the direction form DATA of the specific ncard

    Args:
        numcard(string)
    """
    conn = open_connection()
    cursor = conn.execute("SELECT ncard,username,position,direction FROM DATA WHERE ncard = '%s'" %(numcard))
    direction = cursor.fetchall()[0][3]
    return direction

def insert_initial_data(numcard,username):
    """
    upload numcard and username in START table from the phone

    Args:
        numcard(string)
        username(string)
    """
    conn = open_connection()
    cursor = conn.execute('SELECT ncard,username FROM START WHERE ncard = "%s"' %(numcard))
    if len(cursor.fetchall()) == 0:
        conn.execute('INSERT INTO START VALUES ("%s","%s")' %(numcard,username))
    else:
        conn.execute('UPDATE START SET USERNAME = "%s" WHERE NCARD = "%s"' %(username,numcard))
    conn.commit()
    conn.close()

def get_initial_data(numcard):
    """
    get numcard and username inserted from mobile phone stored in table START

    Args:
        numcard(string)

    Returns:
        cursor(array): cursor[0] is ncard, cursor[1] is username
    """
    conn = open_connection()
    cursor = conn.execute('SELECT * FROM START WHERE NCARD = "%s"' %(numcard))
    row = cursor.fetchall()[0]
    return row

def get_users_positions():
    """
    Retrieves the positions of all the users and their usernames from DATA table

    Returns:
        rows(array of arrays): all rows of the table. Select row (rows[i]) and ncard = rows[i][0], username = rows[i][1]
        position = rows[i][2] direction = rows[i][3]
    """

    conn = open_connection()
    cursor = conn.execute("SELECT ncard,username,position,direction FROM DATA")
    rows = cursor.fetchall()

    return rows

def get_position(numcard):
    """
    Gets user's position from DATA table

    Args:
        numcard(string)

    Returns:

    """
    conn = open_connection()
    cursor = conn.execute("SELECT ncard,username,position,direction FROM DATA WHERE NCARD = '%s'" %(numcard))
    #conn.close()
    pos = cursor.fetchall()[0][2]

    return pos
