import sys
import pygame as pg

from state_engine import Game, GameState
import prepare
import gameplay

states = {"GAMEPLAY": gameplay.Gameplay(),
          "INFO":gameplay.Info(),
          "SHOW":gameplay.Show()}
game = Game(prepare.SCREEN, states, "GAMEPLAY")

game.run()
pg.quit()
sys.exit()
