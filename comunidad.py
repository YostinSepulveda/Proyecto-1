class Comunidad():
    def __init__(self):
        self._num_ciudadanos=None
        self._prom_conexion_fisica=None
        self._prob_conexion_fisica=None
        self._enfermedad=None
        self._num_infectados=None

    def get_num_ciudadanos(self):
        return self._num_ciudadanos

    def set_num_ciudadanos(self, num_ciudadanos):
        self._num_ciudadanos= num_ciudadanos

    def get_prom_conexion_fisica(self):
        return self._prom_conexion_fisica

    def set_prom_conexion_fisica(self,prom_conexion_fisica):
        self._prom_conexion_fisica=prom_conexion_fisica

    def get_prob_conexion_fisica(self):
        return self._prob_conexion_fisica

    def set_prob_conexion_fisica(self,prob_conexion_fisica):
        self._prob_conexion_fisica=prob_conexion_fisica
    
    def get_enfermedad(self):
        return self._enfermedad
    
    def set_enfermedad(self,enfermedad):
        self._enfermedad=enfermedad
        
    def get_num_infectados(self):
        return self._num_infectados
    
    def set_num_infectados(self,num_infectados):
        self._num_infectados=num_infectados
    
    
        
