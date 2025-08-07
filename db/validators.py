import sqlite3

def validation_persona_en_db(person_id):
    conn = sqlite3.connect("mi_base.db")
    cursor = conn.cursor()
    query = "SELECT * FROM Test_Worldsys WHERE personId = ?"
    cursor.execute(query, (person_id,))
    result = cursor.fetchone()
    conn.close()
    return result
