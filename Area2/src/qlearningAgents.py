# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random, util, math

class QLearningAgent(ReinforcementAgent):
    def __init__(self, **args):
        ReinforcementAgent.__init__(self, **args)
        self.qValues = util.Counter()  # Defaults to 0.0

    def getQValue(self, state, action):
        return self.qValues[(state, action)]

    def computeValueFromQValues(self, state):
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return 0.0
        return max([self.getQValue(state, action) for action in legalActions])

    def computeActionFromQValues(self, state):
        legalActions = self.getLegalActions(state)
        if not legalActions:
            return None
        maxQ = self.computeValueFromQValues(state)
        bestActions = [action for action in legalActions if self.getQValue(state, action) == maxQ]
        return random.choice(bestActions)

    def getAction(self, state):
      legalActions = self.getLegalActions(state)
      if not legalActions:
        return None

      if util.flipCoin(self.epsilon):  # Explore
        return random.choice(legalActions)
      else:  # Exploit
        return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        sample = reward + self.discount * self.computeValueFromQValues(nextState)
        self.qValues[(state, action)] = (1 - self.alpha) * self.getQValue(state, action) + self.alpha * sample

class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        features = self.featExtractor.getFeatures(state, action)
        return sum([self.weights[f] * features[f] for f in features])

    def update(self, state, action, nextState, reward):
        features = self.featExtractor.getFeatures(state, action)
        difference = (reward + self.discount * self.getValue(nextState)) - self.getQValue(state, action)
        for f in features:
            self.weights[f] += self.alpha * difference * features[f]

    def final(self, state):
        PacmanQAgent.final(self, state)
        if self.episodesSoFar == self.numTraining:
            print("Final weights:", self.weights)