import numpy as np
import time

from gym_unity.envs import UnityEnv

env_name = "../envs/Cat_2/Cats.exe"


print("\nwith no render")

env = UnityEnv(env_name, no_graphics=False, multiagent=True, worker_id=1)
"""
res = []

for j in range(10):
"""
print(str(env))
ini_obs = env.reset()

curr_t = time.time()

for i in range(10000):
  actions = [env.action_space.sample() for agent in range(env.number_agents)]
  obs, rew, done, info = env.step(actions)

res = time.time() - curr_t

print("\nTime for 1000 step")
print(res)
print("\n\n")
"""
res = []

for j in range(10):

  ini_obs = env.reset()

  curr_t = time.time()

  for i in range(10000):
    done = False
    obs, rew, done, info = env.step(env.action_space.sample())

  res.append(time.time() - curr_t)

print("\n Time for 10000 step")
print(np.asarray(res).mean())
print("\n\n")

res = []

for j in range(10):

  ini_obs = env.reset()

  curr_t = time.time()

  for i in range(100000):
    done = False
    obs, rew, done, info = env.step(env.action_space.sample())

  res.append(time.time() - curr_t)

print("\n Time for 100000 step")
print(np.asarray(res).mean())
print("\n\n")

env.close()

print("\nwithOUT render")

env = UnityEnv(env_name, no_graphics=True)

res = []

for j in range(10):

  ini_obs = env.reset()

  curr_t = time.time()

  for i in range(1000):
    done = False
    obs, rew, done, info = env.step(env.action_space.sample())

  res.append(time.time() - curr_t)

print("\nTime for 1000 step")
print(np.asarray(res).mean())
print("\n\n")

res = []

for j in range(10):

  ini_obs = env.reset()

  curr_t = time.time()

  for i in range(10000):
    done = False
    obs, rew, done, info = env.step(env.action_space.sample())

  res.append(time.time() - curr_t)

print("\n Time for 10000 step")
print(np.asarray(res).mean())
print("\n\n")

res = []

for j in range(10):

  ini_obs = env.reset()

  curr_t = time.time()

  for i in range(100000):
    done = False
    obs, rew, done, info = env.step(env.action_space.sample())

  res.append(time.time() - curr_t)

print("\n Time for 100000 step")
print(np.asarray(res).mean())
print("\n\n")
"""
env.close()