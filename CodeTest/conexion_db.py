#Conexión a Access DB
import pyodbc

conexion = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=DB/momentosHu.accdb;')
#pyodbc.InterfaceError: ('IM002', '[IM002] [Microsoft][ODBC Driver Manager] Data source name not found and no default driver specified (0) (SQLDriverConnect)')


conexion = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=DB/momentosHu.accdb;')

#cursor: objeto usado para ejecutar queries de SQL
cursor = conexion.cursor()
cursor.execute('select * from momentos_hu')

for row in cursor.fetchall():
    print (row)


#SQL: select
#cursor.execute('select * from momentos_hu')

#Una sola fila
#one_row = cursor.fetchone()

#Todas las filas
#rows = cursor.fetchall()