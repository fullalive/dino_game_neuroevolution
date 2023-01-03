# import neat
# import os
from game import Game

game = Game()

game.runGame()

# Load configuration.
# local_dir = os.path.dirname(__file__)
# config_path = os.path.join(local_dir, 'config-feedforward')
# config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

# init NEAT
# n = neat.Population(config)

# run NEAT
# n.run(game.runGame, 1000)