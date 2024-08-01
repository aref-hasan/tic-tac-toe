"""
This script trains a Q-learning agent to play Tic-Tac-Toe. Initially, the agent was trained with fixed hyperparameters 
and no dynamic adjustments. The training process showed stable but not optimal results with a consistent win rate of 
around 75%. 

To improve the agent's performance, several enhancements were made:
1. Dynamic Epsilon-Greedy Strategy: The epsilon value, which determines the exploration rate, is now decayed over time.
   This allows the agent to explore more in the beginning and exploit learned strategies in later stages of training.
2. Hyperparameter Adjustments: Learning rate, discount factor, and epsilon decay parameters were adjusted to improve 
   learning efficiency and stability.
3. Training Progress Monitoring: Added periodic logging to track training progress, including win rates, average rewards, 
   and the current epsilon value.

These changes aimed to enhance the agent's learning process, achieve higher win rates, and provide better insights into 
the training dynamics.

Results:
After the enhancements, the agent achieved a win rate of approximately 78% with an average reward of 1.14 over 50,000 episodes. 
This demonstrates a significant improvement in the agent's performance, indicating that the dynamic epsilon strategy and 
adjusted hyperparameters contributed to better learning and decision-making capabilities.

Aref Hasan
"""

import sys
import os
import pickle

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.q_learning_agent import train_agent, QLearningAgent

if __name__ == "__main__":
    episodes = 50000  # Number of episodes for training
    learning_rate = 0.01  # Learning rate
    discount_factor = 0.95  # Discount factor
    epsilon = 1.0  # Initial epsilon for exploration
    epsilon_min = 0.01  # Minimum epsilon for exploration
    epsilon_decay = 0.995  # Epsilon decay rate

    # Train the Q-learning agent
    agent, win_rates, average_rewards = train_agent(episodes, learning_rate, discount_factor, epsilon, epsilon_min, epsilon_decay, print_interval=1000)
    
    # Save the trained agent
    with open(os.path.join('.', 'models', 'trained_agent.pkl'), 'wb') as f:
        pickle.dump(agent, f)
    
    # Optionally save training metrics for later analysis
    training_metrics = {
        'win_rates': win_rates,
        'average_rewards': average_rewards
    }
    with open(os.path.join('.', 'models', 'training_metrics.pkl'), 'wb') as f:
        pickle.dump(training_metrics, f)
