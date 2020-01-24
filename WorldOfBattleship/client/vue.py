from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics.instructions import InstructionGroup
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.video import Video
from kivy.uix.dropdown import DropDown
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition


class Vue(FloatLayout):

    def __init__(self, controleur, **kwargs):
        super(Vue, self).__init__(**kwargs)
        Window.size = (1280, 720)
        self.eventTirs = None
        self.ori = 0
        self.taille = [2,3,3,4,5]
        self.indice = 0
        self.bateauX = 0
        self.bateauY = 0
        self.viseeX = 0
        self.viseeY = 0

        with self.canvas.before:
            self.video = Video(source='client/ressources/MovieExtend.mp4', state='play', size=self.size)

        self.controleur = controleur
        #self.racine = FloatLayout(size=Constante.TAILLE_FENETRE)
        #bottom
        self.panelPrincipale = BoxLayout(padding=10)
        self.panelIntro = BoxLayout(orientation='vertical', size_hint=(1,0.07), pos_hint={'center_x': 0.5, 'center_y': 0.07})
        self.panelAccueil = BoxLayout(orientation='vertical', spacing=10, size_hint=(1,0.3), pos_hint={'center_x': 0, 'center_y': 0.20})
        self.panelMenuJvsIA = BoxLayout(orientation='vertical', spacing=10, size_hint=(1,0.7), pos_hint={'center_x': 0, 'center_y': 0.5})
        self.panelMenuIAvsIA = BoxLayout(orientation='vertical', spacing=10, size_hint=(1,0.8), pos_hint={'center_x': 0, 'center_y': 0.5})
        self.panelGameJvsIA = BoxLayout(padding=0)
        self.panelGameIAvsIA = BoxLayout(padding=0)
        self.panelOption = BoxLayout(orientation='vertical', spacing=10, size_hint=(1,0.5), pos_hint={'center_x': 0, 'center_y': 0.5})
        self.panelStatsIA = BoxLayout(orientation='vertical', spacing=10, size_hint=(1,0.06), pos_hint={'center_x': 0, 'center_y': 0.035})

        self.buttonJoueurvsJoueur = Button(text='Player VS Player', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=25, size_hint=(0.2,1), pos_hint={'center_x': 0.282})
        self.buttonJoueurvsIA = Button(text='Player VS A.I.', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=25, size_hint=(0.2,1), pos_hint={'center_x': 0.282})
        self.buttonIAvsIA = Button(text='A.I. VS A.I.', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=25, size_hint=(0.2,1), pos_hint={'center_x': 0.282})
        self.buttonSkip = Button(text='Skip', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=15, size_hint=(0.1,1), pos_hint={'center_x': 0.95})
        self.buttonRetourAccueil = Button(text='Home Page', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonRetourAccueil1 = Button(text='Home Page', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonRetourAccueil2 = Button(text='Home Page', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.5})
        self.buttonStartJvsIA = Button(text='Start', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonStartIAvsIA = Button(text='Start', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonOption = Button(text='Option', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonPlus = Button(text='+', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=30, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonMoins = Button(text='-', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=30, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.buttonRetour = Button(text='Done', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})

        self.dropdown = DropDown()
        self.buttonIARandom = Button(text='IARandom', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAProba = Button(text='IAProba', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADecroi = Button(text='IADecroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACroi = Button(text='IACroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADia = Button(text='IADia', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAQua = Button(text='IAQua', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACinq = Button(text='IACinq', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.dropdown.add_widget(self.buttonIARandom)
        self.dropdown.add_widget(self.buttonIAProba)
        self.dropdown.add_widget(self.buttonIADecroi)
        self.dropdown.add_widget(self.buttonIACroi)
        self.dropdown.add_widget(self.buttonIADia)
        self.dropdown.add_widget(self.buttonIAQua)
        self.dropdown.add_widget(self.buttonIACinq)
        self.mainDropDown = Button(text='A.I. Selection', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})

        self.dropdown1 = DropDown()
        self.buttonIARandom1 = Button(text='IARandom', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAProba1 = Button(text='IAProba', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADecroi1 = Button(text='IADecroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACroi1 = Button(text='IACroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADia1 = Button(text='IADia', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAQua1 = Button(text='IAQua', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACinq1 = Button(text='IACinq', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.dropdown1.add_widget(self.buttonIARandom1)
        self.dropdown1.add_widget(self.buttonIAProba1)
        self.dropdown1.add_widget(self.buttonIADecroi1)
        self.dropdown1.add_widget(self.buttonIACroi1)
        self.dropdown1.add_widget(self.buttonIADia1)
        self.dropdown1.add_widget(self.buttonIAQua1)
        self.dropdown1.add_widget(self.buttonIACinq1)
        self.mainDropDown1 = Button(text='A.I. Selection', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})

        self.dropdown2 = DropDown()
        self.buttonIARandom2 = Button(text='IARandom', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAProba2 = Button(text='IAProba', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADecroi2 = Button(text='IADecroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACroi2 = Button(text='IACroi', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIADia2 = Button(text='IADia', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIAQua2 = Button(text='IAQua', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.buttonIACinq2 = Button(text='IACinq', size_hint_y=None, height=44, border = (0,0,0,0), background_normal='client/ressources/DropDownList.png')
        self.dropdown2.add_widget(self.buttonIARandom2)
        self.dropdown2.add_widget(self.buttonIAProba2)
        self.dropdown2.add_widget(self.buttonIADecroi2)
        self.dropdown2.add_widget(self.buttonIACroi2)
        self.dropdown2.add_widget(self.buttonIADia2)
        self.dropdown2.add_widget(self.buttonIAQua2)
        self.dropdown2.add_widget(self.buttonIACinq2)
        self.mainDropDown2 = Button(text='A.I. Selection', border = (0,0,0,0), background_normal='client/ressources/Unselected.png', background_down='client/ressources/Selected.png', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})

        self.textNom = TextInput(hint_text='Player Name', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.textNom.multiline = False
        self.textPartie = TextInput(hint_text='1', input_filter = 'int', font_size=20, size_hint=(0.2,1), pos_hint={'center_x': 0.75})
        self.textPartie.multiline = False
        self.labelNom = Label(text='Enter your Player Name', font_size=25, bold=True, pos_hint={'center_x': 0.75})
        self.labelSelection = Label(text="\n\nA.I. Selection\n", font_size=25, bold=True, pos_hint={'center_x': 0.75})
        self.labelSpace = Label(text=" \n", font_size=30, bold=True, pos_hint={'center_x': 0.75})
        self.labelSelection1 = Label(text="\nA.I. n°1 Selection\n", font_size=25, bold=True, pos_hint={'center_x': 0.75})
        self.labelSpace1 = Label(text=" \n", font_size=30, bold=True, pos_hint={'center_x': 0.75})
        self.labelSelection2 = Label(text="\nA.I. n°2 Selection\n", font_size=25, bold=True, pos_hint={'center_x': 0.75})
        self.labelSpace2 = Label(text=" \n", font_size=30, bold=True, pos_hint={'center_x': 0.75})
        self.labelOption = Label(text="Number of games\n", font_size=25, bold=True, pos_hint={'center_x': 0.75})
        self.labelSpace3 = Label(text=" \n", font_size=30, bold=True, pos_hint={'center_x': 0.75})

        self.panelIntro.add_widget(self.buttonSkip)

        self.panelAccueil.add_widget(self.buttonJoueurvsJoueur)
        self.panelAccueil.add_widget(self.buttonJoueurvsIA)
        self.panelAccueil.add_widget(self.buttonIAvsIA)

        self.panelMenuJvsIA.add_widget(self.labelNom)
        self.panelMenuJvsIA.add_widget(self.textNom)
        self.panelMenuJvsIA.add_widget(self.labelSelection)
        self.panelMenuJvsIA.add_widget(self.mainDropDown)
        self.panelMenuJvsIA.add_widget(self.labelSpace)
        self.panelMenuJvsIA.add_widget(self.buttonStartJvsIA)
        self.panelMenuJvsIA.add_widget(self.buttonRetourAccueil)

        self.panelMenuIAvsIA.add_widget(self.labelSelection1)
        self.panelMenuIAvsIA.add_widget(self.mainDropDown1)
        self.panelMenuIAvsIA.add_widget(self.labelSelection2)
        self.panelMenuIAvsIA.add_widget(self.mainDropDown2)
        self.panelMenuIAvsIA.add_widget(self.labelSpace2)
        self.panelMenuIAvsIA.add_widget(self.buttonStartIAvsIA)
        self.panelMenuIAvsIA.add_widget(self.buttonOption)
        self.panelMenuIAvsIA.add_widget(self.buttonRetourAccueil1)

        self.panelOption.add_widget(self.labelOption)
        self.panelOption.add_widget(self.buttonPlus)
        self.panelOption.add_widget(self.textPartie)
        self.panelOption.add_widget(self.buttonMoins)
        self.panelOption.add_widget(self.labelSpace3)
        self.panelOption.add_widget(self.buttonRetour)

        self.panelStatsIA.add_widget(self.buttonRetourAccueil2)

        self.add_widget(self.panelPrincipale)

        Clock.schedule_once(self.afficheIntro, 1)

    def afficheIntro(self, dt):
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.add_widget(self.panelIntro)

    def affichePanelAccueil(self):
        self.panelPrincipale.canvas.before.clear()
        self.panelPrincipale.canvas.clear()
        self.panelPrincipale.canvas.after.clear()
        self.panelPrincipale.clear_widgets()
        with self.panelPrincipale.canvas.before:
            self.video2 = Video(source='client/ressources/accueil.mp4', state='play', size=(1280, 736), eos='loop', volume=0)
        with self.panelPrincipale.canvas.after:
            self.wimg = Image(source='client/ressources/Logo.png', size=(244,244), pos=(243.5,280))
            self.anim = Animation(x=243.5,y=275) +  Animation(x=244,y=285)
            self.anim.repeat = True
            self.anim.start(self.wimg)
            self.img = Image(source='client/ressources/World_of_Battleship_nologo.png', size=(571.5,215), pos=(80,450))
        self.panelPrincipale.add_widget(self.panelAccueil)

    def affichePanelJoueurVsIA(self):
        print('Trying to get keyboard')
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        print('Trying to get keyboard done')
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.canvas.before.clear()
        self.panelPrincipale.canvas.after.clear()
        self.panelGameJvsIA.clear_widgets()
        self.video2.unload()
        self.panelBateaux = GridLayout(cols = 10, padding=30, size_hint=(1,0.7), pos_hint={'center_x': 0.25})
        self.panelTirs = GridLayout(cols = 10, padding=30, size_hint=(1,0.7), pos_hint={'center_x': 0.75})
        self.B = []
        self.T = []
        for i in range(100):
            self.B.append(Button(text='B ' + str(int(i/10)) + ' ' + str(i%10), background_normal='client/ressources/Unselected.png'))
            self.T.append(Button(text='T ' + str(int(i/10)) + ' ' + str(i%10), background_normal='client/ressources/Unselected.png'))
            self.panelBateaux.add_widget(self.B[i])
            self.panelTirs.add_widget(self.T[i])
        self.panelGameJvsIA.add_widget(self.panelBateaux)
        self.panelGameJvsIA.add_widget(self.panelTirs)
        with self.panelPrincipale.canvas.before:
            self.backgound = Image(source='client/ressources/gameBackground.png', size=self.size)
            rotateText = Label(text='Press R to rotate boats', font_size=50, bold=True, pos=(600,100), opacity=0)
            anim = Animation(opacity=1, duration=1) + Animation(duration=3) + Animation(opacity=0, duration=1)
            anim.start(rotateText)
        self.panelPrincipale.add_widget(self.panelGameJvsIA)
        self.eventPlacement = Clock.schedule_interval(self.triggerPlacementBateaux, 0.1)
        for i in range(len(self.T)):
            self.T[i].disabled = True

    def affichePanelIAvsIA(self):
        print('Trying to get keyboard')
        self.keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
        print('Trying to get keyboard done')
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.add_widget(self.panelGameIAvsIA)
        self.panelPrincipale.canvas.before.clear()
        self.panelPrincipale.canvas.clear()
        self.panelPrincipale.canvas.after.clear()
        self.video2.unload()
        with self.panelPrincipale.canvas.before:
            self.backgound = Image(source='client/ressources/gameBackground2.png', size=self.size)

    def affichePanelOption(self):
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.add_widget(self.panelOption)

    def affichePanelStatsIA(self, J1, J2, minmaxJ1, minmaxJ2):
        self.panelPrincipale.canvas.after.clear()
        self.panelPrincipale.clear_widgets()
        with self.panelPrincipale.canvas.after:
            self.tabStat = Image(source='client/ressources/Stats.png', size=self.size)

            nomJ1 = Label(text=str(J1[0]), font_size=30, bold=True, pos=(350,600))
            pourcentJ1 = Label(text='Percentage of victory = ' + str(round(J1[1]*100,3)) + '%', font_size=25, bold=True, pos=(350,500))
            coupMinJ1 = Label(text='Minimum number of shots = ' + str(minmaxJ1[1]), font_size=25, bold=True, pos=(350,400))
            coupMaxJ1 = Label(text='Maximum number of shots = ' + str(minmaxJ1[0]), font_size=25, bold=True, pos=(350,300))
            coupMoyJ1 = Label(text='Average number of shots = ' + str(round(J1[2],3)), font_size=25, bold=True, pos=(350,200))

            nomJ2 = Label(text=str(J2[0]), font_size=30, bold=True, pos=(850,600))
            pourcentJ2 = Label(text='Percentage of victory = ' + str(round(J2[1]*100,3)) + '%', font_size=25, bold=True, pos=(850,500))
            coupMinJ2 = Label(text='Minimum number of shots = ' + str(minmaxJ2[1]), font_size=25, bold=True, pos=(850,400))
            coupMaxJ2 = Label(text='Maximum number of shots = ' + str(minmaxJ2[0]), font_size=25, bold=True, pos=(850,300))
            coupMoyJ2 = Label(text='Average number of shots = ' + str(round(J2[2],3)), font_size=25, bold=True, pos=(850,200))

            nbParties = Label(text='Number of games : ' + str(self.textPartie.text), font_size=25, bold=True, pos=(600,100))

        self.panelPrincipale.add_widget(self.panelStatsIA)

    def startPartieJvsIA(self):
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.add_widget(self.panelMenuJvsIA)

    def startPartieIAvsIA(self):
        self.panelPrincipale.clear_widgets()
        self.panelPrincipale.add_widget(self.panelMenuIAvsIA)

    def triggerPlacementBateaux(self, dt):
        self.placementBateaux(self.ori, self.indice+1, self.taille[self.indice])

    def placementBateaux(self, ori, indice, taille): #Ajouter argument ori, indice et taille
        self.panelPrincipale.canvas.clear()
        correction = 0
        if taille == 2:
            taille = 3
            correction = 1
        if taille == 4:
            taille = 5
            correction = 1
        if ori == 0:
            taille0 = int(taille/2)
            taille1 = 0
        else :
            taille0 = 0
            taille1 = int(taille/2)

        if Window.mouse_pos[0] >= (40.0 + taille0*57 - correction*57) and Window.mouse_pos[0] < (610.0 - taille0*57) and Window.mouse_pos[1] >= (40.0 + taille1*43 - correction*43) and Window.mouse_pos[1] < (469.0 - taille1*43):
            if Window.mouse_pos[0] < 40 or Window.mouse_pos[1] < 40:
                pass
            else :
                for i in range(10):
                    if Window.mouse_pos[0] >= 40+57*i and Window.mouse_pos[0] < 97+57*i:
                        self.bateauX = 68 + i * 57
                    if Window.mouse_pos[1] >= 40+43*i and Window.mouse_pos[1] < 83+43*i:
                        self.bateauY = 61 + i * 43
                with self.panelPrincipale.canvas:
                    self.follow = Image(source='client/ressources/Bateaux/Bateau'+str(indice)+'_'+str(ori)+'.png')
                    self.follow.size = (self.follow.texture.size[0]/1.5, self.follow.texture.size[1]/(1.5+0.5*ori))
                    self.follow.pos = (self.bateauX - self.follow.size[0]/2, self.bateauY - self.follow.size[1]/2)

    def inscriptionBateaux(self):
        with self.panelPrincipale.canvas.after:
            self.boat = Image(source='client/ressources/Bateaux/Bateau'+str(self.indice+1)+'_'+str(self.ori)+'.png')
            self.boat.size = (self.boat.texture.size[0]/1.5, self.boat.texture.size[1]/(1.5+0.5*self.ori))
            self.boat.pos = (self.bateauX - self.boat.size[0]/2, self.bateauY - self.boat.size[1]/2)

    def objectifTir(self, dt):
        self.panelPrincipale.canvas.clear()
        if Window.mouse_pos[0] >= 670.0 and Window.mouse_pos[0] < 1240.0 and Window.mouse_pos[1] >= 40.0 and Window.mouse_pos[1] < 469.0:
            for i in range(10):
                if Window.mouse_pos[0] >= 670+57*i and Window.mouse_pos[0] < 727+57*i:
                    self.viseeX = 698 + i * 57
                if Window.mouse_pos[1] >= 40+43*i and Window.mouse_pos[1] < 83+43*i:
                    self.viseeY = 61 + i * 43
            with self.panelPrincipale.canvas:
                self.follow = Image(source='client/ressources/Cible.png')
                self.follow.size = (self.follow.texture.size[0]/1.5, self.follow.texture.size[1]/1.5)
                self.follow.pos = (self.viseeX - self.follow.size[0]/2, self.viseeY - self.follow.size[1]/2)

    def missed(self):
        with self.panelPrincipale.canvas.after:
            self.follow = Image(source='client/ressources/Missed.png')
            self.follow.size = (self.follow.texture.size[0]/1.5, self.follow.texture.size[1]/1.5)
            self.follow.pos = (self.viseeX - self.follow.size[0]/2, self.viseeY - self.follow.size[1]/2)

    def touched(self):
        with self.panelPrincipale.canvas.after:
            self.follow = Image(source='client/ressources/Explosion.png')
            self.follow.size = (self.follow.texture.size[0]/1.5, self.follow.texture.size[1]/1.5)
            self.follow.pos = (self.viseeX - self.follow.size[0]/2, self.viseeY - self.follow.size[1]/2)

    def textSink(self):
        with self.panelPrincipale.canvas.after:
            sink = Label(text='Sunk !', font_size=50, bold=True, pos=(600,100), opacity=0)
            anim = Animation(opacity=1, duration=0.2) + Animation(duration=1) + Animation(opacity=0, duration=0.2)
            anim.start(sink)

    def affichageBateauxIA1(self, pos, i):
        with self.panelPrincipale.canvas :
            lenght = len(pos[i])//2
            if pos[i][1][0] - pos[i][0][0] == 1 or pos[i][1][0] - pos[i][0][0] == -1:
                ori = 1
                if (i == 0 and pos[0][0][0] > pos[0][1][0]) or (i == 3 and pos[3][0][0] > pos[3][1][0]):
                    lenght = (len(pos[i])//2)-1
            else :
                ori = 0
                if (i == 0 and pos[0][0][1] < pos[0][1][1]) or (i == 3 and pos[3][0][1] < pos[3][1][1]):
                    lenght = (len(pos[i])//2)-1

            x = 57 + pos[i][lenght][1] * 43.46
            y = 331.5 - pos[i][lenght][0] * 32.86
            self.boat = Image(source='client/ressources/Bateaux/Bateau'+str(i+1)+'_'+str(ori)+'.png')
            self.boat.size = (self.boat.texture.size[0]/2, self.boat.texture.size[1]/(2+0.5*ori))
            self.boat.pos = (x - self.boat.size[0]/2, y - self.boat.size[1]/2)

    def affichageBateauxIA2(self, pos, i):
        with self.panelPrincipale.canvas :
            lenght = len(pos[i])//2
            if pos[i][1][0] - pos[i][0][0] == 1 or pos[i][1][0] - pos[i][0][0] == -1:
                ori = 1
                if (i == 0 and pos[0][0][0] > pos[0][1][0]) or (i == 3 and pos[3][0][0] > pos[3][1][0]):
                    lenght = (len(pos[i])//2)-1
            else :
                ori = 0
                if (i == 0 and pos[0][0][1] < pos[0][1][1]) or (i == 3 and pos[3][0][1] < pos[3][1][1]):
                    lenght = (len(pos[i])//2)-1

            x = 829 + pos[i][lenght][1] * 43.46
            y = 331.5 - pos[i][lenght][0] * 32.86
            self.boat = Image(source='client/ressources/Bateaux/Bateau'+str(i+1)+'_'+str(ori)+'.png')
            self.boat.size = (self.boat.texture.size[0]/2, self.boat.texture.size[1]/(2+0.5*ori))
            self.boat.pos = (x - self.boat.size[0]/2, y - self.boat.size[1]/2)

    def affichageTirsIA1(self, tirs, i, j):
        with self.panelPrincipale.canvas.after:
            x = 56 + j * 43.46
            y = 689 - i * 32.86
            if tirs[i][j] == 'M':
                self.imageM = Image(source = 'client/ressources/Missed.png')
                self.imageM.size = (self.imageM.texture.size[0]/2, self.imageM.texture.size[1]/2)
                self.imageM.pos = (x - self.imageM.size[0]/2, y - self.imageM.size[1]/2)
            elif tirs[i][j] == 'T':
                self.imageT = Image(source = 'client/ressources/Explosion.png')
                self.imageT.size = (self.imageT.texture.size[0]/2, self.imageT.texture.size[1]/2)
                self.imageT.pos = (x - self.imageT.size[0]/2, y - self.imageT.size[1]/2)

    def affichageTirsIA2(self, tirs, i, j):
        with self.panelPrincipale.canvas.after:
            x = 828.5 + j * 43.46
            y = 689 - i * 32.86
            if tirs[i][j] == 'M':
                self.imageM = Image(source = 'client/ressources/Missed.png')
                self.imageM.size = (self.imageM.texture.size[0]/2, self.imageM.texture.size[1]/2)
                self.imageM.pos = (x - self.imageM.size[0]/2, y - self.imageM.size[1]/2)
            elif tirs[i][j] == 'T':
                self.imageT = Image(source = 'client/ressources/Explosion.png')
                self.imageT.size = (self.imageT.texture.size[0]/2, self.imageT.texture.size[1]/2)
                self.imageT.pos = (x - self.imageT.size[0]/2, y - self.imageT.size[1]/2)

    def endGame(self, state, nb, winner):
        with self.panelPrincipale.canvas.after:
            anim = Animation(opacity=1, duration=2)
            if state == 'v' or state == 'ia':
                victory = Image(source= 'client/ressources/Victory.png', opacity = 0, size=self.size)
                anim.start(victory)
            elif state == 'l' :
                loose = Image(source= 'client/ressources/Defeat.png', opacity = 0, size=self.size)
                anim.start(loose)
            win = Label(text='Winner : ' + str(winner), opacity=0, font_size=25, bold=True, pos=(600,200))
            nbCoups = Label(text='Number of shots : ' + str(nb), opacity=0, font_size=25, bold=True, pos=(600,150))
            enter = Label(text='Press Enter to continue...', opacity = 0, font_size=20, bold=True, pos=(1000,50))
            anim.start(win)
            anim.start(nbCoups)
            animEnter = Animation(opacity=1, duration=1) + Animation(opacity=0.2, duration=1)
            animEnter.repeat = True
            animEnter.start(enter)

    def mousePos(self, dt):
        print (Window.mouse_pos)

    def _keyboard_closed(self):
        print('Mon clavier est ferme')
