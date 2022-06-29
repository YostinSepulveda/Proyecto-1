import main
class Persona():
    def __init__(self):
        self._comunidad=None
        self._id=0
        self._familia=None
        self._enfermedad=None
        self._enfermo=False
        self._enfermable=True
        self._contador_curado=0
        self._estado=False
        
    def get_comunidad(self):
        return self._comunidad
    
    def set_comunidad(self,comunidad):
        self._comunidad=comunidad
                
    def get_familia(self):
        return self._familia

    def set_familia(self,familia):
        self._familia=familia
        
    def get_enfermedad(self):
        return self._enfermedad

    def set_enfermedad(self,enfermedad):
        self._enfermedad=enfermedad
        
    def get_estado(self):
        return self._estado

    def set_estado(self,estado):
        self._estado=estado
        
    def get_enfermo(self):
        return self._enfermo

    def set_enfermo(self,enfermo):
        self._enfermo=enfermo
    
    def get_enfermable(self):
        return self._enfermable

    def set_enfermable(self,enfermable):
        self._enfermable=enfermable
    
    def get_contador_curado(self):
        return self._contador_curado
    
    def set_contador_curado(self,contador_curado):
        self._contador_curado=contador_curado
    
    def comp_contador(self):
        if self.get_contador_curado >= main.covid.get_promedio_pasos:
            return True
        return False
    
    
        
    

    



        