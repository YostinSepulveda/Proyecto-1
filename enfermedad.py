class Enfermedad():
    def __init__(self):
        self._infeccion_probable=None
        self._promedio_pasos=None
        self._enfermo=False
        self._contador=0
        
    def get_infeccion_probable(self):
        return self._infeccion_probable

    def set_infeccion_probable(self,infeccion_probable):
        self._infeccion_probable=infeccion_probable
                
    def get_promedio_pasos(self):
        return self._promedio_pasos

    def set_promedio_pasos(self,promedio_pasos):
        self._promedio_pasos=promedio_pasos
            
    def get_enfermo(self):
        return self._enfermo

    def set_enfermo(self,enfermo):
        self._enfermo=enfermo

    def get_contador(self):
        return self._contador

    def set_contador(self,contador):
        self._contador=contador
