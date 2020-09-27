# -*- coding: utf-8 -*-
"""
  mda_base.py generated by WhatsOpt 1.10.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 3


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from mda.structure import Structure
from mda.aerodynamics import Aerodynamics
from mda.propulsion import Propulsion





class MdaBase(Group):
    """ An OpenMDAO base component to encapsulate Mda MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(MdaBase, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['err_on_non_converge'] = False
        self.nonlinear_solver.options['reraise_child_analysiserror'] = False

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['err_on_non_converge'] = False
        self.linear_solver.options['iprint'] = 1

    def setup(self): 

        self.add_subsystem('Structure', self.create_structure(), promotes=['L', 'sigma', 'Theta', 'WE', 'WF', 'WT', 'x_str', 'z'])
        self.add_subsystem('Aerodynamics', self.create_aerodynamics(), promotes=['D', 'dpdx', 'ESF', 'fin', 'L', 'Theta', 'WT', 'x_aer', 'z'])
        self.add_subsystem('Propulsion', self.create_propulsion(), promotes=['D', 'DT', 'ESF', 'SFC', 'Temp', 'WE', 'x_pro', 'z'])

    def create_structure(self):
    	return Structure()
    def create_aerodynamics(self):
    	return Aerodynamics()
    def create_propulsion(self):
    	return Propulsion()


# Used by Thrift server to serve disciplines
class MdaFactoryBase(object):
    @staticmethod
    def create_mda_structure():
    	return Structure()
    @staticmethod
    def create_mda_aerodynamics():
    	return Aerodynamics()
    @staticmethod
    def create_mda_propulsion():
    	return Propulsion()
