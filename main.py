from comunidad import Comunidad
from enfermedad import Enfermedad
covid= Enfermedad()
covid.set_infeccion_probable(0.3)
covid.set_promedio_pasos(5)

talca= Comunidad()
talca.set_num_ciudadanos(2000)
talca.set_prob_conexion_fisica(0.4)
talca.set_prom_conexion_fisica(4)
talca.set_enfermedad("Covid")
talca.set_num_infectados(10)
