from persona import Persona
from enfermedad import Enfermedad
from comunidad import Comunidad
import main
import random
class Simulador():
    def __init__(self):

        pasos=45
        personas_comunidad=[]
        for i in range(main.talca.get_num_ciudadanos()):
            personas_comunidad.append(Persona())
            
        for x in personas_comunidad:
            x.set_comunidad(main.talca)
            x.set_familia(random.randint(0,main.talca.get_num_ciudadanos()/5))
            x.set_enfermedad(main.covid)
        c=1
        for x in personas_comunidad:
            x.set_enfermo(True)
            x.set_enfermable(False)
            c=c+1
            if c==main.talca.get_num_infectados():
                break
        print("Paso 0")
        print("enfermos",main.talca.get_num_infectados())
        print("enfermables",main.talca.get_num_ciudadanos()-main.talca.get_num_infectados())
        print("sanados 0")
         ############################################################################################   
        
        for z in range(pasos):
            print("Paso",z+1)
            enfermos=0
            enfermables=0
            sanados=0
            for x in personas_comunidad:
                if x.get_contador_curado()==main.covid.get_promedio_pasos():
                    x.set_enfermo(False)
                    x.set_estado(True)
            
              
            for i in personas_comunidad:
                if i.get_enfermo()==True:
                    for l in range(main.talca.get_prom_conexion_fisica()):
                        y=random.randint(1,10)
                        if y<=(main.talca.get_prob_conexion_fisica()*10):
                            k=random.randint(1,10)
                            if k<=(main.covid.get_infeccion_probable()*10):
                                p=random.randint(0,main.talca.get_num_ciudadanos())
                                c=0
                                for x in personas_comunidad:
                                    if p==c:
                                        if x.get_enfermable()==True:
                                            x.set_enfermo(True)
                                            x.set_enfermable(False)
                                            break
                                    c=c+1
                                    
            for x in personas_comunidad:
                if x.get_enfermo()==True:
                    x.set_contador_curado(x.get_contador_curado()+1)
                    enfermos=enfermos+1 

                elif x.get_enfermable()==True:
                    enfermables=enfermables+1
                else:
                    sanados=sanados+1
        
            
            print ("enfermos",enfermos)
            print ("enfermables",enfermables)
            print ("sanados",sanados)

    
    

if 1==1:
    sim=Simulador()
