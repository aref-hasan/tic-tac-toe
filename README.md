# Tic-Tac-Toe Q-Learning Agent

# Tic-Tac-Toe Q-Learning Agent

![Tic-Tac-Toe Demo](tic_tac_toe.gif)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 

### AI Course - Assignment 3

#### Author: [Aref Hasan](https://github.com/aref-hasan) 

## Project Overview

This project is developed as part of the AI course and represents the third assignment. The goal is to create a Q-Learning agent capable of playing Tic-Tac-Toe. The agent learns to play the game through reinforcement learning, specifically using the Q-Learning algorithm. The project involves training the agent, evaluating its performance, and visualizing the results.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Training the Agent](#training-the-agent)
- [Evaluating the Agent](#evaluating-the-agent)
- [Playing Against the Agent](#playing-against-the-agent)
- [Results](#results)
- [License](#license)


## Installation


To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd tic_tac_toe_rl


2. **Create a virtual environment**:
    ```python3 -m venv venv
    source venv/bin/activate  # on Windows, use `venv\Scripts\activate`


3. **Install the required packages**:
    ```pip install -r requirements.txt

    
## Training the Agent
To train the Q-Learning agent, run the train.py script located in the scripts directory. The script trains the agent for a specified number of episodes and saves the trained model.
    ```python scripts/train.py


## Evaluating the Agent
To evaluate the trained agent, use the Jupyter notebook evaluate.ipynb located in the notebooks directory. 


## Playing Against the Agent
To play against the trained Q-Learning agent, run the play_gui.py script located in the gui directory. This script starts a graphical user interface where you can play Tic-Tac-Toe against the agent.
    ```python gui/play_gui.py





## Results


### Training Results
Initially, the agent was trained with fixed hyperparameters and no dynamic adjustments. The training process showed stable but not optimal results with a consistent win rate of around 75%.

To improve the agent's performance, several enhancements were made:

1. Dynamic Epsilon-Greedy Strategy: The epsilon value, which determines the exploration rate, is now decayed over time. This allows the agent to explore more in the beginning and exploit learned strategies in later stages of training.

2. Hyperparameter Adjustments: Learning rate, discount factor, and epsilon decay parameters were adjusted to improve learning efficiency and stability.

3. Training Progress Monitoring: Added periodic logging to track training progress, including win rates, average rewards, and the current epsilon value.


After the enhancements, the agent achieved a win rate of approximately 78% with an average reward of 1.14 over 50,000 episodes. This demonstrates a significant improvement in the agent's performance, indicating that the dynamic epsilon strategy and adjusted hyperparameters contributed to better learning and decision-making capabilities.

## License
This project is licensed under the MIT License - see the [License](LICENSE) file for details.