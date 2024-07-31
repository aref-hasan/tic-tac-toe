import random
import numpy as np

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
        # initialize Q-table as a regular dictionary
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

    def get_q_values(self, state):
        # convert state to a string key and return Q-values, initializing if necessary
        state_key = str(state)
        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(9)
        return self.q_table[state_key]

    def choose_action(self, state, available_actions):
        if random.uniform(0, 1) < self.epsilon:
            # explore: choose a random action
            return random.choice(available_actions)
        # exploit: choose the best action from the Q-table
        q_values = self.get_q_values(state)
        return available_actions[np.argmax(q_values[available_actions])]

    def update_q_table(self, state, action, reward, next_state, done):
        q_values = self.get_q_values(state)
        next_q_values = self.get_q_values(next_state)
        best_next_action = np.argmax(next_q_values)
        # calculate the TD target
        td_target = reward + self.discount_factor * next_q_values[best_next_action] * (1 - done)
        # update the Q-value
        td_error = td_target - q_values[action]
        q_values[action] += self.learning_rate * td_error

def train_agent(episodes=10000):
    from models.tic_tac_toe import TicTacToe
    env = TicTacToe()
    agent = QLearningAgent()
    for episode in range(episodes):
        state = env.reset()
        done = False
        while not done:
            available_actions = env.available_actions()
            action = agent.choose_action(state, available_actions)
            next_state, reward, done = env.step(action)
            agent.update_q_table(state, action, reward, next_state, done)
            state = next_state
    return agent
