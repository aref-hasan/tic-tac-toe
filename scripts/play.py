import sys
import os
import pickle
import random

#parent directory and current directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.tic_tac_toe import TicTacToe

def play_game(agent):
    env = TicTacToe()
    state = env.reset()
    done = False
    while not done:
        #agent's turn
        available_actions = env.available_actions()
        action = agent.choose_action(state, available_actions)
        state, reward, done = env.step(action)
        env.render()
        if done:
            if reward == 1:
                print("Agent wins!")
            elif reward == 2:
                print("Random player wins!")
            else:
                print("It's a draw!")
            break
        
        #human player's turn
        if not done:
            print("Enter your action (0-8): ")
            human_action = int(input().strip())
            while human_action not in available_actions:
                print("Invalid action! Enter your action (0-8): ")
                human_action = int(input().strip())
            state, reward, done = env.step(human_action)
            env.render()
            if done:
                if reward == 1:
                    print("Agent wins!")
                elif reward == 2:
                    print("Random player wins!")
                else:
                    print("It's a draw!")

if __name__ == "__main__":
    #trained agent
    with open('models/trained_agent.pkl', 'rb') as f:
        agent = pickle.load(f)
    #play a game with the trained agent
    play_game(agent)
