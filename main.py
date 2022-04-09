# This is a sample Python script.

import gym

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    env = gym.make('ALE/Tennis-v5',
                   obs_type='rgb',  # ram | rgb | grayscale
                   frameskip=5,  # frame skip
                   mode=0,  # game mode, see Machado et al. 2018
                   difficulty=0,  # game difficulty, see Machado et al. 2018
                   repeat_action_probability=0.25,  # Sticky action probability
                   full_action_space=True,  # Use all actions
                   render_mode='human'  # None | human | rgb_array
                   )

    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample())  # take a random action
    env.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
