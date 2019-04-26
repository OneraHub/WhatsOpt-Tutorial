# -*- coding: utf-8 -*-
"""
  constraints_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 2

import numpy as np
from openmdao.api import ExplicitComponent

class ConstraintsBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Constraints discipline """

    def setup(self):
        self.add_input('DT', val=np.ones((1,)), desc='')
        self.add_input('ESF', val=np.ones((1,)), desc='')
        self.add_input('Temp', val=np.ones((1,)), desc='')
        self.add_input('Theta', val=np.ones((1,)), desc='')
        self.add_input('dpdx', val=np.ones((1,)), desc='')
        self.add_input('sigma', val=np.ones((5,)), desc='')

        self.add_output('con1_esf', val=np.ones((1,)), desc='')

        self.add_output('con2_esf', val=np.ones((1,)), desc='')

        self.add_output('con_dpdx', val=np.ones((1,)), desc='')

        self.add_output('con_dt', val=np.ones((1,)), desc='')

        self.add_output('con_sigma1', val=np.zeros((1,)), desc='')

        self.add_output('con_sigma2', val=np.zeros((1,)), desc='')

        self.add_output('con_sigma3', val=np.zeros((1,)), desc='')

        self.add_output('con_sigma4', val=np.zeros((1,)), desc='')

        self.add_output('con_sigma5', val=np.zeros((1,)), desc='')

        self.add_output('con_temp', val=np.ones((1,)), desc='')

        self.add_output('con_theta_low', val=np.ones((1,)), desc='')

        self.add_output('con_theta_up', val=np.ones((1,)), desc='')
        self.declare_partials('*', '*', method='cs')

        