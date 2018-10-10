from kivy.clock import Clock
from functools import partial
from kivy.core.window import Window
from client.vue import Vue
from game.partie import *


class Controleur:
    
    def __init__(self):
        self.vue = Vue(self, size=(1280, 720))
        self.partiePredef = PartiePredef()
        self.client = None
        self.i = 0
        self.i2 = 0
        
        self.vue.buttonSkip.bind(on_release=self.actionSkip)
        self.vue.buttonRetourAccueil.bind(on_release=self.actionRetourAccueil)
        self.vue.buttonRetourAccueil1.bind(on_release=self.actionRetourAccueil)
        self.vue.buttonRetourAccueil2.bind(on_release=self.actionRetourAccueil)
        self.vue.buttonJoueurvsJoueur.bind(on_release=self.actionRetourAccueil)
        self.vue.buttonIAvsIA.bind(on_release=self.actionButtonIAvsIA)
        self.vue.buttonJoueurvsIA.bind(on_release=self.actionButtonJoueurvsIA)
        self.vue.buttonOption.bind(on_release=self.actionButtonOption)
        self.vue.buttonPlus.bind(on_release=self.actionButtonPlus)
        self.vue.buttonMoins.bind(on_release=self.actionButtonMoins)
        self.vue.buttonRetour.bind(on_release=self.actionButtonRetour)
        self.vue.buttonStartJvsIA.bind(on_release=self.actionButtonStartJvsIA)
        self.vue.buttonStartIAvsIA.bind(on_release=self.actionButtonStartIAvsIA)
        
        self.vue.buttonIARandom.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIARandom.text))
        self.vue.buttonIAProba.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIAProba.text))
        self.vue.buttonIADecroi.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIADecroi.text))
        self.vue.buttonIACroi.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIACroi.text))
        self.vue.buttonIADia.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIADia.text))
        self.vue.buttonIAQua.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIAQua.text))
        self.vue.buttonIACinq.bind(on_release=lambda btn: self.vue.dropdown.select(self.vue.buttonIACinq.text))
        self.vue.mainDropDown.bind(on_release=self.vue.dropdown.open)
        self.vue.dropdown.bind(on_select=lambda instance, x: setattr(self.vue.mainDropDown, 'text', x))
        
        self.vue.buttonIARandom1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIARandom1.text))
        self.vue.buttonIAProba1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIAProba1.text))
        self.vue.buttonIADecroi1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIADecroi1.text))
        self.vue.buttonIACroi1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIACroi1.text))
        self.vue.buttonIADia1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIADia1.text))
        self.vue.buttonIAQua1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIAQua1.text))
        self.vue.buttonIACinq1.bind(on_release=lambda btn: self.vue.dropdown1.select(self.vue.buttonIACinq1.text))
        self.vue.mainDropDown1.bind(on_release=self.vue.dropdown1.open)
        self.vue.dropdown1.bind(on_select=lambda instance, x: setattr(self.vue.mainDropDown1, 'text', x))
        
        self.vue.buttonIARandom2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIARandom2.text))
        self.vue.buttonIAProba2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIAProba2.text))
        self.vue.buttonIADecroi2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIADecroi2.text))
        self.vue.buttonIACroi2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIACroi2.text))
        self.vue.buttonIADia2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIADia2.text))
        self.vue.buttonIAQua2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIAQua2.text))
        self.vue.buttonIACinq2.bind(on_release=lambda btn: self.vue.dropdown2.select(self.vue.buttonIACinq2.text))
        self.vue.mainDropDown2.bind(on_release=self.vue.dropdown2.open)
        self.vue.dropdown2.bind(on_select=lambda instance, x: setattr(self.vue.mainDropDown2, 'text', x))
    
    def actionRetourAccueil(self, instance):
        self.vue.video2.unload()
        self.vue.canvas.before.clear()
        self.vue.affichePanelAccueil()
        self.partiePredef.__init__()
    
    def actionSkip(self, instance):
        self.vue.video.unload()
        self.vue.affichePanelAccueil()
    
    def actionButtonStartJvsIA(self, instance):  # Button Start menu JvsIA
        self.partiePredef.nomJ = self.vue.textNom.text
        self.partiePredef.joueur1 = self.partiePredef.inputJoueur('J')
        self.partiePredef.joueur2 = self.partiePredef.inputJoueur(self.vue.mainDropDown.text)
        self.partie = Partie(self.partiePredef.joueur1, self.partiePredef.joueur2)
        self.partiePredef.Parties.append(self.partie)
        self.vue.affichePanelJoueurVsIA()
        for i in range(100):
            self.vue.B[i].bind(on_press=self.choixPlacement)
            self.vue.T[i].bind(on_press=self.choixTir)
        self.vue.keyboard.bind(on_key_down=self.actionToucheClavier)
    
    def actionButtonStartIAvsIA(self, instance):  # Button Start menu IAvsIA
        self.partiePredef.joueur1 = self.partiePredef.inputJoueur(self.vue.mainDropDown1.text)
        self.partiePredef.joueur2 = self.partiePredef.inputJoueur(self.vue.mainDropDown2.text)
        if self.vue.textPartie.text == '' or self.vue.textPartie.text == '1':
            self.vue.affichePanelIAvsIA()
            self.eventBateau = Clock.schedule_interval(self.triggerBateauxIA1, 0.1)
            self.partie = Partie(self.partiePredef.joueur1, self.partiePredef.joueur2)
            self.partiePredef.Parties.append(self.partie)
            self.vue.keyboard.bind(on_key_down=self.actionToucheClavier)
        else:
            self.partiePredef.nb = int(self.vue.textPartie.text)
            self.partiePredef.Start()
            minmaxJ1 = [self.partiePredef.minmax(self.partiePredef.J1[0])[0],
                        self.partiePredef.minmax(self.partiePredef.J1[0])[1]]
            minmaxJ2 = [self.partiePredef.minmax(self.partiePredef.J2[0])[0],
                        self.partiePredef.minmax(self.partiePredef.J2[0])[1]]
            self.vue.affichePanelStatsIA(self.partiePredef.J1, self.partiePredef.J2, minmaxJ1, minmaxJ2)
    
    def triggerBateauxIA1(self, dt):
        self.vue.affichageBateauxIA1(self.partie.joueurs[0].Bateaux.pos, self.i)
        self.i += 1
        if self.i == 5:
            self.eventBateau.cancel()
            self.eventBateau2 = Clock.schedule_interval(self.triggerBateauxIA2, 0.1)
            self.i = 0
    
    def triggerBateauxIA2(self, dt):
        self.vue.affichageBateauxIA2(self.partie.joueurs[1].Bateaux.pos, self.i2)
        self.i2 += 1
        if self.i2 == 5:
            self.eventBateau2.cancel()
            self.eventTour = Clock.schedule_interval(self.triggerTourIA, 0.1)
            self.i2 = 0
    
    def triggerTourIA(self, dt):
        self.partiePredef.result.append(self.partiePredef.Parties[0].Tour(True, 1))
        
        if self.partie.current == 0:
            self.vue.affichageTirsIA1(self.partie.joueurs[0].tabTirs, self.partie.joueurs[0].tirX,
                                      self.partie.joueurs[0].tirY)
        else:
            self.vue.affichageTirsIA2(self.partie.joueurs[1].tabTirs, self.partie.joueurs[1].tirX,
                                      self.partie.joueurs[1].tirY)
        
        if self.partie.winner[0] == True:
            self.eventTour.cancel()
            self.vue.endGame('ia', self.partie.nbTours, self.partie.joueurs[self.partie.winner[1]].nom)
    
    def actionButtonJoueurvsIA(self, instance):  # Button JvsIA accueil
        self.vue.startPartieJvsIA()
    
    def actionButtonIAvsIA(self, instance):  # Button IAvsIA accueil
        self.vue.startPartieIAvsIA()
    
    def actionButtonPlus(self, instance):
        if self.vue.textPartie.text == '':
            self.vue.textPartie.text = self.vue.textPartie.hint_text
        self.vue.textPartie.text = str(int(self.vue.textPartie.text) + 1)
    
    def actionButtonMoins(self, instance):
        if self.vue.textPartie.text == '':
            self.vue.textPartie.text = self.vue.textPartie.hint_text
        if int(self.vue.textPartie.text) - 1 < 1:
            self.vue.textPartie.text == 1
        else:
            self.vue.textPartie.text = str(int(self.vue.textPartie.text) - 1)
    
    def actionButtonRetour(self, instance):
        self.vue.startPartieIAvsIA()
    
    def actionButtonOption(self, instance):
        self.vue.affichePanelOption()
    
    def choixPlacement(self, instance):
        split = instance.text.split()
        
        if self.vue.ori == 0:
            sens = 'E'
            ajustementX = 0
            if self.vue.taille[self.vue.indice] == 2:
                ajustementY = 0
            elif self.vue.taille[self.vue.indice] == 3 or self.vue.taille[self.vue.indice] == 4:
                ajustementY = 1
            if self.vue.taille[self.vue.indice] == 5:
                ajustementY = 2
        elif self.vue.ori == 1:
            sens = 'N'
            ajustementY = 0
            if self.vue.taille[self.vue.indice] == 2:
                ajustementX = 0
            elif self.vue.taille[self.vue.indice] == 3 or self.vue.taille[self.vue.indice] == 4:
                ajustementX = -1
            if self.vue.taille[self.vue.indice] == 5:
                ajustementX = -2
        
        self.partie.joueurs[0].Bateaux.pos[self.vue.indice] = self.partie.joueurs[0].Bateaux.placement(
            int(split[1]) - ajustementX, int(split[2]) - ajustementY, sens, self.vue.taille[self.vue.indice])
        
        if not self.partie.joueurs[0].Bateaux.pos[self.vue.indice] == []:
            self.vue.inscriptionBateaux()
            self.vue.indice += 1
        
        if self.vue.indice >= 5:
            self.vue.eventPlacement.cancel()
            self.vue.indice = 0
            self.vue.eventTirs = Clock.schedule_interval(self.vue.objectifTir, 0.1)
            for i in range(len(self.vue.B)):
                self.vue.B[i].disabled = True
                self.vue.T[i].disabled = False
        
        print(self.partie.joueurs[0].Bateaux.pos)
        print('Button <%s> is pressed' % instance.text)
    
    def choixTir(self, instance):
        split = instance.text.split()
        self.partie.joueurs[0].tirX = int(split[1])
        self.partie.joueurs[0].tirY = int(split[2])
        
        self.partiePredef.result.append(self.partiePredef.Parties[0].Tour(True, 1))  # Tour joueur
        if self.partie.joueurs[0].tabTirs[self.partie.joueurs[0].tirX][self.partie.joueurs[0].tirY] == 'T':
            self.vue.touched()
            if self.partie.joueurs[0].coule == True:
                self.vue.textSink()
                self.partie.joueurs[0].coule = False
        else:
            self.vue.missed()
        
        if self.partie.winner[0] == True:
            self.vue.eventTirs.cancel()
            for i in range(len(self.vue.B)):
                self.vue.T[i].disabled = True
            self.vue.endGame('v', self.partie.nbTours, self.partie.joueurs[self.partie.winner[1]].nom)
            return
        
        self.partiePredef.result.append(self.partiePredef.Parties[0].Tour(True, 1))  # Tour IA
        if self.partie.joueurs[1].tabTirs[self.partie.joueurs[1].tirX][self.partie.joueurs[1].tirY] == 'T':
            self.vue.viseeX = 68 + self.partie.joueurs[1].tirY * 57
            self.vue.viseeY = 61 + (9 - self.partie.joueurs[1].tirX) * 43
            self.vue.touched()
        else:
            self.vue.viseeX = 68 + self.partie.joueurs[1].tirY * 57
            self.vue.viseeY = 61 + (9 - self.partie.joueurs[1].tirX) * 43
            self.vue.missed()
        
        if self.partie.winner[0] == True:
            self.vue.eventTirs.cancel()
            for i in range(len(self.vue.B)):
                self.vue.T[i].disabled = True
            self.vue.endGame('l', self.partie.nbTours, self.partie.joueurs[self.partie.winner[1]].nom)
        
        # print('Button <%s> is pressed' % instance.text)
    
    def actionToucheClavier(self, keyboard, keycode, text, modifiers):
        
        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        print('ActionTouchClavier ' + str(keycode))
        if keycode[1] == 'escape':
            keyboard.release()
        
        if keycode[1] == 'r':
            if self.vue.ori == 0:
                self.vue.ori = 1
            else:
                self.vue.ori = 0
        
        if keycode[1] == 'enter' and self.partie.winner[0] == True:
            self.vue.affichePanelAccueil()
            self.partiePredef.__init__()
        
        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True
