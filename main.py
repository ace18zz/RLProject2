import gym

if __name__ == '__main__':

    ''' Initialise environnment '''
    env = gym.make('PongNoFrameskip-v4',
                    obs_type='grayscale',  # ram | rgb | grayscale
                    frameskip=4,  # frame skip
                    mode=0,  # game mode, see Machado et al. 2018
                    difficulty=0,  # game difficulty, see Machado et al. 2018
                    repeat_action_probability=0.25,  # Sticky action probability
                    full_action_space=False,  # Use all actions
                    render_mode='human'  # None | human | rgb_array
                    )
    print("Old observation Space: ", env.observation_space.shape) #(210, 160)

    ''' Downsample the observation to 84 x 84 pixels '''
    env = gym.wrappers.AtariPreprocessing(env,
                                          noop_max=30,
                                          frame_skip=4,
                                          screen_size=84,
                                          terminal_on_life_loss=False,
                                          grayscale_obs=True,
                                          grayscale_newaxis=False,
                                          scale_obs=False)

    ''' Stack 4 frames together for observation'''
    env = gym.wrappers.FrameStack(env, 4)

    print("New observation Space: ", env.observation_space.shape) #(4, 84, 84)
    print("Action Space       ", env.action_space.shape)
    print("Possible action: {} {}".format(env.action_space.n, env.unwrapped.get_action_meanings()))

    ''' Record the game '''
    #env = gym.wrappers.Monitor(env, 'recording', force=True)

    ''' Play n episode '''
    n = 10
    for i_episode in range(n):
        env.reset()
        Return = 0
        for t in range(1000):
            env.render()
            observation, reward, done, info = env.step(env.action_space.sample())
            Return = Return + reward
            if done:
                print("Episode: {} Episode finished after {} timesteps. Return: {}".format(i_episode, t + 1, Return))
                break
    env.close()
