
#clase usuario 

class usuario:
     #constructor 
     def  __init__(self,nombre,apellido,cedula,edad) :
            self.nombre=nombre
            self.apellido=apellido
            self.cedula=cedula
            self.edad=edad
       
     def detalle_Usuario (self ):
         return  "propietario de la cuenta "+self.nombre+" "+self.apellido+"\n"+"idenatificaciòn  Cc:"+str(self.cedula)+"\nedad "+str(self.edad)

#calse cuenta

class cuenta (usuario):

    #constructor 
    def __init__(self, nombre, apellido, cedula, edad,cantidad_de_dinero_ahorrado):
         usuario.__init__(self,nombre,apellido,cedula,edad)
         self.ahorro=cantidad_de_dinero_ahorrado
    
    #metodos de classe cuenta 
    def mostrar (self ):
         return  "propietario de la cuenta "+self.nombre+" "+self.apellido+"\n"+"idenatificaciòn  Cc:"+str(self.cedula)+"\nsaldo "+str(self.ahorro)+"$"

    def ingresar (self,consignacion):
        if consignacion<0:
            return "no es posible consignar valores negativos"
        else: 
            self.ahorro=consignacion+self.ahorro
            return  "propietario de la cuenta "+self.nombre+" "+self.apellido+"\n el nuevo saldo es saldo "+str(self.ahorro)+"$"


    def retirar (self, consignacion):
        if consignacion<0:
            return "no es posible retirar valores negativos"
        else: 
             self.ahorro=self.ahorro-consignacion
             return  "propietario de la cuenta "+self.nombre+" "+self.apellido+"\n el nuevo saldo es "+str(self.ahorro)+"$"


   # def get(self):
    #    return self.nombre,self.apellido,self.cedula,self.edad,self.ahorro
   
   # metodos gets(para indicar contenido ) 
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getCedula(self):
        return self.cedula
    def getEdad(self):
        return self.edad
    def getAhorro(self):
        return self.ahorro

### metodos sets(para actualizar)  
    def setNombre(self,nombre):
        self.nombre=nombre
    def setApellido(self,apellido):
        self.apellido=apellido
    def setCedula(self,cedula):
        self.cedula=cedula
    def setEdad(self,edad):
        self.edad=edad
    def setAhorro(self,ahorro):
        self.ahorro=ahorro


class beneficio():
 pass





        