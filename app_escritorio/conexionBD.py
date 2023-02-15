import mysql.connector

class Datos:
    # Conectarse al servidor MySQL
    def __init__(self):
        self.conexion = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='proyecto_mineros')

    def obtenerEmpleados(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM empleado" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def obtenerRegistroEmpleado(self):
        cursor = self.conexion.cursor()
        sql = '''SELECT e.CED_EMP, e.NOM_EMP, e.APE_EMP, r.FECHA_ENTRADA, r.PATH 
                FROM empleado as e  
                INNER JOIN registro_empleado as r ON e.CED_EMP = r.CED_EMP'''
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def insertarEmpleado(self,cedula, nombre, apellido, fechaNac):
        cur = self.conexion.cursor()
        sql='''INSERT INTO empleado (CED_EMP, NOM_EMP, APE_EMP, FECHA_NAC) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(cedula, nombre, apellido, fechaNac)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def insertarRegistroAsistencia(self,cedula, fechaEntrada, casco, chaleco, botas, observacion, path):
        cur = self.conexion.cursor()
        sql='''INSERT INTO registro_empleado (CED_EMP, FECHA_ENTRADA, CASCO, CHALECO, BOTAS, OBSERVACION, PATH) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(cedula, fechaEntrada, casco, chaleco, botas, observacion, path)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
