import numpy as np

priors     = np.array([0.5,0.3,0.2])
transition = np.array([[0.85, 0.05,0.1],
                       [0.05, 0.9,0.05],
                        [1/2, 1/4, 1/4]])
emission   = np.array([[0.699, 0.05, 0.1, 0.05, 0.1, 0.001],
                    [0.001, 0.1, 0.1, 0.299, 0.3, 0.2],
                       [0.1, 0.2, 0.1, 0.2, 0.1, 0.3]])

hmm_params = {'priors': priors,
               'transition': transition,
                'emission': emission}

problem_dict = {'attacker': 'sd',
                 't': 3}


unc_dict = {'rho': np.array([0.75,0.75,0.75,0.75,0.75,0.75]),
                 'k': 100 ,
                   'N1': 10000, 
                'N2': 5000}

params_dict = {'ratio': {'init_rt': 0.1,
                        'fn_rt':  110,
                       'rt_st':  0.1},
              'contour': {'start_w1': 0.1,
                          'stop_w1': 3,
                          'n_values_w1': 3,
                           'start_w2': 0.1,
                            'stop_w2':3,
                              'n_values_w2':3},
                'box': True}


X_obs = np.array([ [4], [3], [5], [3], [4]])