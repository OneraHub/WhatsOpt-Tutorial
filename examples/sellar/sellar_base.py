# -*- coding: utf-8 -*-
"""
  sellar_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 1

import numpy as np
from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS, ScipyKrylov
from openmdao_extensions.reckless_nonlinear_block_gs import RecklessNonlinearBlockGS

from disc1 import Disc1
from disc2 import Disc2
from functions import Functions

class SellarBase(Group):
    """ An OpenMDAO base component to encapsulate Sellar MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(SellarBase, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['maxiter'] = 10
        self.nonlinear_solver.options['iprint'] = 1
        self.linear_solver = ScipyKrylov()
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['maxiter'] = 10
        self.linear_solver.options['iprint'] = 1

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('x', 2)
        indeps.add_output('z', [5, 2])
        self.add_subsystem('Disc1', self.create_disc1(), promotes=['x', 'z', 'y1', 'y2'])
        self.add_subsystem('Disc2', self.create_disc2(), promotes=['z', 'y1', 'y2'])
        self.add_subsystem('Functions', self.create_functions(), promotes=['x', 'z', 'y1', 'y2', 'f', 'g1', 'g2'])

    def create_disc1(self):
    	return Disc1()
    def create_disc2(self):
    	return Disc2()
    def create_functions(self):
    	return Functions()


# Used by Thrift server to serve disciplines
class SellarFactoryBase(object):
    @staticmethod
    def create_disc1():
    	return Disc1()
            
    @staticmethod
    def create_disc2():
    	return Disc2()
            
    @staticmethod
    def create_functions():
    	return Functions()
            
