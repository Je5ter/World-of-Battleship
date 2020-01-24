import kivy
from kivy.app import App
from client.controleur import Controleur

kivy.require('1.11.1')  # Replace with your current kivy version !


class Game(App):

    def build(self):

        controleur = Controleur()

        return controleur.vue


if __name__ == '__main__':
    game = Game()
    game.run()
