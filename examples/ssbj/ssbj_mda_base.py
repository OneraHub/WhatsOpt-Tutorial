# -*- coding: utf-8 -*-
"""
  ssbj_mda_base.py generated by WhatsOpt 1.10.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 2


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from mda.mda import Mda
from performance import Performance
from constraints import Constraints
from mda.structure import Structure
from mda.aerodynamics import Aerodynamics
from mda.propulsion import Propulsion




class SsbjMdaBase(Group):
    """ An OpenMDAO base component to encapsulate SsbjMda MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(SsbjMdaBase, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 0.001
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['err_on_non_converge'] = False
        self.nonlinear_solver.options['reraise_child_analysiserror'] = False

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['err_on_non_converge'] = False
        self.linear_solver.options['iprint'] = 1

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('x_aer', 1.0)
        indeps.add_output('x_pro', 1.0)
        indeps.add_output('x_str', [1.0, 1.0])
        indeps.add_output('z', [1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        self.add_subsystem('Mda', self.create_mda(), promotes=['D', 'dpdx', 'DT', 'ESF', 'fin', 'L', 'SFC', 'sigma', 'Temp', 'Theta', 'WE', 'WF', 'WT', 'x_aer', 'x_pro', 'x_str', 'z'])
        self.add_subsystem('Performance', self.create_performance(), promotes=['fin', 'R', 'SFC', 'WF', 'WT', 'z'])
        self.add_subsystem('Constraints', self.create_constraints(), promotes=['con1_esf', 'con2_esf', 'con_dpdx', 'con_dt', 'con_sigma1', 'con_sigma2', 'con_sigma3', 'con_sigma4', 'con_sigma5', 'con_temp', 'con_theta_low', 'con_theta_up', 'dpdx', 'DT', 'ESF', 'sigma', 'Temp', 'Theta'])

    def create_mda(self):
    	return Mda()


    def create_performance(self):
    	return Performance()
    def create_constraints(self):
    	return Constraints()


# Used by Thrift server to serve disciplines
class SsbjMdaFactoryBase(object):
    @staticmethod
    def create_performance():
    	return Performance()
    @staticmethod
    def create_constraints():
    	return Constraints()
    @staticmethod
    def create_mda_structure():
    	return Structure()
    @staticmethod
    def create_mda_aerodynamics():
    	return Aerodynamics()
    @staticmethod
    def create_mda_propulsion():
    	return Propulsion()
