import com_function as cf


def validateUser(role, id):
    dbCursor = cf.connect()
    dbCursor.execute(f"""SELECT * FROM {role} WHERE {role}_number = '{id}'""")
    user = dbCursor.fetchone()
    if user:
        return True
    else:
        cf.warningWindow("Login failed")
        return False
    
def registerStaff(id):
    
