import sqlite3
import datetime

sql_db_path = 'MIMEs/Data'
sql_db = 'Test1234.db'
sql_db_name = sql_db_path + '/' + sql_db


def sql_initialize(  ):
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    cur.execute ("SELECT name FROM sqlite_master WHERE type='table';")
    l_avail_tables = cur.fetchall()
    
    # print ( l_avail_tables )

    # check for table_pass
    if [table for table in l_avail_tables if table[0] == 'table_pass'] != [] :
        pass
    else :
        sql_cmd = 'CREATE TABLE table_pass (id VARCHAR , hashed_key VARCHAR)'
        cur.execute( sql_cmd )
        conn.commit()
        sql_cmd = 'INSERT INTO table_pass (id, hashed_key ) VALUES ("Admin","$pbkdf2-sha256$30000$z5lTqrW2FsJY6z0HIGTsvQ$UQPX1a4iVPbFfiSTe3vwVKve3SIXgjRXDYK6lU8V8kk")'
        cur.execute(sql_cmd)
        conn.commit()
        
    # check for table_recharge
    if [table for table in l_avail_tables if table[0] == 'table_recharge'] != [] :
        pass
    else :
        sql_cmd = 'CREATE TABLE table_recharge (ID INTEGER PRIMARY KEY AUTOINCREMENT, txn_dt DATETIME , product VARCHAR , ec_amt NUMERIC , added_amt NUMERIC , comment VARCHAR)'
        cur.execute( sql_cmd )
        conn.commit()
    
    # check for table_payment
    if [table for table in l_avail_tables if table[0] == 'table_payment'] != [] :
        pass
    else :
        sql_cmd = 'CREATE TABLE table_payment (ID INTEGER PRIMARY KEY AUTOINCREMENT, txn_dt DATETIME , product VARCHAR , pay_amt NUMERIC  , comment VARCHAR)'
        cur.execute( sql_cmd )
        conn.commit()

    # check for table_dailybalance
    if [table for table in l_avail_tables if table[0] == 'table_dailybalance'] != [] :
        pass
    else :
        sql_cmd = 'CREATE TABLE table_dailybalance ( ID INTEGER PRIMARY KEY AUTOINCREMENT , txn_dt DATETIME  , p_jio NUMERIC , p_airtel NUMERIC , p_vodafone NUMERIC , p_multi NUMERIC , p_sundirect NUMERIC , comment VARCHAR)'
        cur.execute( sql_cmd )
        conn.commit()

    conn.close()

def read_credentials( user_id ):
    result =0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT hashed_key FROM table_pass where id ='" + user_id +"';"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    if (len(result)) > 0:
        (result,)= result[0]
    else:
        result = ''
    return result

def read_recharge_table():
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, product, ec_amt, added_amt, comment FROM table_recharge ;"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    return result

def read_recharge_table_by_ID( id ):
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, product, ec_amt, added_amt, comment FROM table_recharge where ID = "+ str( id )+";"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    
    if (len(result)) > 0:
        [result]= result
    else:
        result = ''
    return result


def upsert_recharge_table( id , txn_date , product , ec_amt , added_amt  , comment ):
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    txn_date = txn_date.strftime("%Y-%m-%d")

    if str(id) == '' :
        sql_command = 'INSERT INTO table_recharge (txn_dt, product, ec_amt, added_amt, comment) VALUES ("'+ txn_date +'","'+ product + '",' + ec_amt + ',' + added_amt +',"'+comment+'") ;'
    else:
        sql_command = 'update table_recharge set ID = '+ id +', txn_dt = "'+ txn_date +'", product = "'+ product +'" , ec_amt = '+ ec_amt +', added_amt = '+ added_amt +', comment = "'+ comment +'"  where ID = '+ id +';'
    cur.execute(sql_command)
    conn.commit()
    conn.close()


def read_payment_table():
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, product, pay_amt, comment FROM table_payment ;"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    return result

def read_payment_table_by_ID( id ):
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, product, pay_amt, comment FROM table_payment where ID = "+ str( id )+";"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    
    if (len(result)) > 0:
        [result]= result
    else:
        result = ''
    return result

def upsert_payment_table( id , txn_date , product , pay_amt  , comment ):
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    txn_date = txn_date.strftime("%Y-%m-%d")

    if str(id) == '' :
        sql_command = 'INSERT INTO table_payment (txn_dt, product, pay_amt, comment) VALUES ("'+ txn_date +'","'+ product + '",' + pay_amt +',"'+comment+'") ;'
    else:
        sql_command = 'update table_payment set ID = '+ id +', txn_dt = "'+ txn_date +'", product = "'+ product +'" , pay_amt = '+ pay_amt + ', comment = "'+ comment +'"  where ID = '+ id +';'
    cur.execute(sql_command)
    conn.commit()
    conn.close()

def read_dailybalance_table():
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, p_jio , p_airtel , p_vodafone , p_multi , p_sundirect , comment FROM table_dailybalance ;"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    return result

def read_dailybalance_table_by_ID( id ):
    result = 0
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    sql_command = "SELECT ID , txn_dt, p_jio , p_airtel , p_vodafone , p_multi , p_sundirect , comment FROM table_dailybalance where ID = "+ str( id )+";"
    cur.execute(sql_command)
    result =cur.fetchall()
    conn.close()
    
    if (len(result)) > 0:
        [result]= result
    else:
        result = ''
    return result

def upsert_dailybalance_table( id , txn_date , p_jio , p_airtel , p_vodafone , p_multi , p_sundirect , comment ):
    conn = sqlite3.connect( sql_db_name )
    cur = conn.cursor()
    txn_date = txn_date.strftime("%Y-%m-%d")

    if str(id) == '' :
        sql_command = 'INSERT INTO table_dailybalance (  txn_dt  , p_jio , p_airtel , p_vodafone , p_multi , p_sundirect , comment ) VALUES ("'+ txn_date +'",'+ p_jio + ',' + p_airtel + ',' + p_vodafone+ ',' + p_multi+ ',' + p_sundirect+',"'+comment+'") ;'
    else:
        sql_command = 'update table_dailybalance set ID = '+ id +', txn_dt = "'+ txn_date +'", p_jio = '+ p_jio +' , p_airtel = '+ p_airtel +' , p_vodafone = '+ p_vodafone +' , p_multi = '+ p_multi +' , p_sundirect = '+ p_sundirect + ', comment = "'+ comment +'"  where ID = '+ id +';'
    cur.execute(sql_command)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    sql_initialize()
    print('SQL Initialized')