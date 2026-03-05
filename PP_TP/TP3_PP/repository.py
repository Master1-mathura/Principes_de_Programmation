from db import get_connection

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return result