import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from about import About
from numbify import NumberEntry
from stepsWindow import askForSteps
"""from comunidad import Comunidad
from enfermedad import Enfermedad
from persona import Persona"""

class Core(Gtk.Window):
    def __init__(self):

        # Builder - Conf. Inicial
        super().__init__()
        self.set_default_size(1228,720)
        self.set_border_width(20)
        self.set_resizable(False)

        # Boton - About
        btn_about = Gtk.Button(label="[?]")
        btn_about.connect("clicked", self.aboutShow)

        # Boton - Resize
        btn_resize = Gtk.Button(label="⧉")
        btn_resize.connect("clicked", self.resize)
    
        # HeaderBar
        self.header = Gtk.HeaderBar(title = "Nombre del proyecto I")
        self.header.set_subtitle("Listo para iniciar simulación")
        self.header.props.show_close_button = True

        self.header.pack_start(btn_about)
        self.header.pack_end(btn_resize)

        self.set_titlebar(self.header)

        # Boton - Iniciar Simulacion
        btn_start = Gtk.Button(label="⋄ Iniciar ⋄")
        btn_start.connect("clicked", self.start)

        # Labels
        '''Comunidad'''
        self.lbl_community = Gtk.Label()
        self.lbl_community.set_markup("<b><big>Comunidad</big></b>")

        self.lbl_community_name = Gtk.Label(label="Nombre de la comunidad")
        self.lbl_community_population = Gtk.Label(label="Población")
        self.lbl_community_promContact = Gtk.Label(label="Promedio contacto físico")
        self.lbl_community_probContact = Gtk.Label(label="Probabilidad contacto físico")
        self.lbl_community_initialIfected = Gtk.Label(label="Infectados Iniciales")

        '''Enfermedad'''
        self.lbl_disease = Gtk.Label()
        self.lbl_disease.set_markup("<b><big>Enfermedad</big></b>")

        self.lbl_disease_probInfection = Gtk.Label(label="Probabilidad de infección")
        self.lbl_disease_stepsEvolution = Gtk.Label(label="Pasos antes de la evolución")

        # Entrys
        '''Comunidad'''
        self.ent_community_name = Gtk.Entry()
        self.ent_community_name.connect("changed", self.updateLabelStatus)

        self.ent_community_population = NumberEntry()
        self.ent_community_population.set_input_purpose(2)
        self.ent_community_population.connect("changed", self.updateLabelStatus)

        self.ent_community_promContact = NumberEntry()
        self.ent_community_promContact.set_input_purpose(2)
        self.ent_community_promContact.connect("changed", self.updateLabelStatus)

        self.ent_community_probContact = NumberEntry()
        self.ent_community_probContact.set_input_purpose(2)
        self.ent_community_probContact.connect("changed", self.updateLabelStatus)

        self.ent_community_initialInfected = NumberEntry()
        self.ent_community_initialInfected.set_input_purpose(2)
        self.ent_community_initialInfected.connect("changed", self.updateLabelStatus)

        '''Enfermedad'''
        self.ent_disease_probInfection = NumberEntry()
        self.ent_disease_probInfection.set_input_purpose(2)
        self.ent_disease_probInfection.connect("changed", self.updateLabelStatus)

        self.ent_disease_stepsEvolution = NumberEntry()
        self.ent_disease_stepsEvolution.set_input_purpose(2)
        self.ent_disease_stepsEvolution.connect("changed", self.updateLabelStatus)

        parameters_community = [self.lbl_community,
                                self.lbl_community_name,
                                self.ent_community_name,
                                self.lbl_community_population,
                                self.ent_community_population,
                                self.lbl_community_promContact,
                                self.ent_community_promContact,
                                self.lbl_community_probContact,
                                self.ent_community_probContact,
                                self.lbl_community_initialIfected,
                                self.ent_community_initialInfected]

        parameters_disease = [self.lbl_disease,
                              self.lbl_disease_probInfection,
                              self.ent_disease_probInfection,
                              self.lbl_disease_stepsEvolution,
                              self.ent_disease_stepsEvolution]
                                
        self.entrys = [self.ent_community_name,
                       self.ent_community_population,
                       self.ent_community_promContact,
                       self.ent_community_probContact,
                       self.ent_community_initialInfected,
                       self.ent_disease_probInfection,
                       self.ent_disease_stepsEvolution]
        
        self.labels = [self.lbl_community_name,
                       self.lbl_community_population,
                       self.lbl_community_promContact,
                       self.lbl_community_probContact,
                       self.lbl_community_initialIfected,
                       self.lbl_disease_probInfection,
                       self.lbl_disease_stepsEvolution]

        # Treeview - Visor resultados resumidos
        self.lss_results = Gtk.ListStore(int,   # Paso
                                         int,   # Casos Activos
                                         int,   # Casos Totales
                                         int,   # Muertos
                                         int)   # Curados

        trv_results = Gtk.TreeView(model = self.lss_results)

        for i, column_title in enumerate(["Paso",
                                          "Casos Activos",
                                          "Casos Totales", 
                                          "Muertos",
                                          "Curados"]):

            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            trv_results.append_column(column)

        # Contenedores
        """Contenedor de parametros"""
        box_parameters_community = Gtk.Box(orientation = 1, spacing = 5)
        for widget in parameters_community:
            box_parameters_community.pack_start(widget,False,True,2)


        box_parameters_disease = Gtk.Box(orientation = 1, spacing = 5)
        for widget in parameters_disease:
            box_parameters_disease.pack_start(widget,False,True,2)

        box_parameters = Gtk.Box(orientation = 1, spacing = 40)
        box_parameters.pack_start(box_parameters_community,True,True,0)
        box_parameters.pack_start(box_parameters_disease,True,True,0)
        box_parameters.pack_start(btn_start,True,True,0)

        
        """Contenedor de resultados"""
        rll_results = Gtk.ScrolledWindow()
        rll_results.set_vexpand(True)
        rll_results.set_hexpand(True)

        rll_results.add(trv_results)

        '''Contenedor Principal'''
        box = Gtk.Box(orientation = 0, spacing = 20)
        box.pack_start(box_parameters,True,True,0)
        box.pack_start(rll_results,True,True,0)

        self.add(box)

    def updateLabelStatus(self, widget):
        for i,widget in enumerate(self.entrys):
            if widget.get_text() != "":
                defaultText = self.labels[i].get_text().replace("[!]","")

                self.labels[i].set_text(defaultText)

    # Fun - Alerta Esenciales Vacios
    def checkEsencials(self):
        checked = True
        for i, widget in enumerate(self.entrys):
            if widget.get_text() == "":
                
                checked = False
                if not "!" in self.labels[i].get_text():

                    alertText = "[!]"+self.labels[i].get_text() + "[!]"
                    self.labels[i].set_text(alertText)
                    
                
        return checked

    # Fun - Iniciar Simulacion
    def start(self,widget):
        if self.checkEsencials():
            self.header.set_subtitle("Comprobado")
            self.steps = askForSteps(self)
            self.se= askForSteps.aceptar(esto)
        
        else:
            self.header.set_subtitle("Revisa los parámetros")

    # Fun - Cambiar tamaño de la ventana
    def resize(self, widget):
        for i in self.get_size():
            if i == 1228:
                self.set_size_request(800,600)
            if i == 748:
                self.set_size_request(1280,720)


    # Fun - Mostrar dialogo about
    def aboutShow(self, widget):
        About(self)


# Ejecución core
main = Core()
main.connect("destroy", Gtk.main_quit)
main.show_all()
Gtk.main()