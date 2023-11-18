from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v0', apply_api_compatibility=True, render_mode="human")
env = JoypadSpace(env, SIMPLE_MOVEMENT)
done = True
for step in range(100000):
# Start the game to begin with
    if done:
        env.reset()
observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
done = terminated or truncated
env.render()
env.close()


# preprossing Environment


# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
#  pip install stable-baselines3[extra]

from gym.wrappers import FrameStack, GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack,DummyVecEnv
from matplotlib import pyplot as plt



