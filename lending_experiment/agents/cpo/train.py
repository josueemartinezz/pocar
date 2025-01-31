# from argparse import ArgumentParser
# from envs.point_gather import PointGatherEnv
# import gym
# import torch
# from yaml import load, full_load

# from agents.cpo import CPO
# from lending_experiment.config import CLUSTER_PROBABILITIES, GROUP_0_PROB, BANK_STARTING_CASH, INTEREST_RATE, \
#     CLUSTER_SHIFT_INCREMENT
# from lending_experiment.environments.lending_params import DelayedImpactParams, two_group_credit_clusters
# from memory import Memory
# from models import build_diag_gauss_policy, build_mlp
# from simulators import SinglePathSimulator
# from torch_utils.torch_utils import get_device


# config_filename = 'config.yaml'

# parser = ArgumentParser(prog='train.py',
#                         description='Train a policy on the specified environment' \
#                         ' using Constrained Policy Optimization (Achaim 2017).')
# parser.add_argument('--continue', dest='continue_from_file', action='store_true',
#                     help='Set this flag to continue training from a previously ' \
#                     'saved session. Session will be overwritten if this flag is ' \
#                     'not set and a saved file associated with model-name already ' \
#                     'exists.')
# parser.add_argument('--model-name', type=str, dest='model_name', required=True,
#                     help='The entry in config.yaml from which settings' \
#                     'should be loaded.')
# parser.add_argument('--simulator', dest='simulator_type', type=str, default='single-path',
#                     choices=['single-path', 'vine'], help='The type of simulator' \
#                     ' to use when collecting training experiences.')
# args = parser.parse_args()
# continue_from_file = args.continue_from_file
# model_name = args.model_name
# config = full_load(open(config_filename, 'r'))[model_name]

# state_dim = config['state_dim']
# action_dim = config['action_dim']

# n_episodes = config['n_episodes']
# env_name = config['env_name']
# n_episodes = config['n_episodes']
# n_trajectories = config['n_trajectories']
# trajectory_len = config['max_timesteps']
# policy_dims = config['policy_hidden_dims']
# vf_dims = config['vf_hidden_dims']
# cf_dims = config['cf_hidden_dims']
# max_constraint_val = config['max_constraint_val']
# bias_red_cost = config['bias_red_cost']
# device = get_device()

# N_LOCATIONS = 10
# N_ATTENTION_UNITS = 6
# EP_TIMESTEPS = 1000
# # INCIDENT_RATES = [8, 6, 4, 3, 1.5]
# INCIDENT_RATES = [8, 6, 4, 3, 1.5, 8, 6, 4, 3, 1.5]
# DYNAMIC_RATE = 0.1
# PHI = 5

# state_dim = N_LOCATIONS * 4 * PHI
# action_dim = N_LOCATIONS

# policy = build_diag_gauss_policy(state_dim, policy_dims, action_dim)
# value_fun = build_mlp(state_dim + 1, vf_dims, 1)
# cost_fun = build_mlp(state_dim + 1, cf_dims, 1)

# policy.to(device)
# value_fun.to(device)
# cost_fun.to(device)



# env_params = DelayedImpactParams(
#     applicant_distribution=two_group_credit_clusters(
#         cluster_probabilities=CLUSTER_PROBABILITIES,
#         group_likelihoods=[GROUP_0_PROB, 1 - GROUP_0_PROB]),
#     bank_starting_cash=BANK_STARTING_CASH,
#     interest_rate=INTEREST_RATE,
#     cluster_shift_increment=CLUSTER_SHIFT_INCREMENT,
# )

# simulator = SinglePathSimulator(env_name, policy, n_trajectories, trajectory_len, params=env_params)

# # print(simulator.env[0].observation_space.shape)
# # print(simulator.env[0].action_space.shape)

# cpo = CPO(policy, value_fun, cost_fun, simulator, model_name=model_name,
#           bias_red_cost=bias_red_cost, max_constraint_val=max_constraint_val)

# print(f'Training policy {model_name} on {env_name} environment...\n')

# cpo.train(n_episodes)
