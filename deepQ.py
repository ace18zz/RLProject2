class deepQ:
    def __init__(self, action):
        self.action = action
        self.starting_ep = 1.0
        self.ending_ep = 0.1
        self.observe = 50000
        self.explore = 1000000
        self.replayBuffer = deque()

