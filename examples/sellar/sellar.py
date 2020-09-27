# -*- coding: utf-8 -*-
"""
  sellar.py generated by WhatsOpt. 
"""
from optparse import OptionParser
from openmdao.api import Problem
from openmdao.api import NonlinearBlockGS, ScipyKrylov
from openmdao.visualization.n2_viewer.n2_viewer import n2
from openmdao_extensions.reckless_nonlinear_block_gs import RecklessNonlinearBlockGS
from sellar_base import SellarBase, SellarFactoryBase

class Sellar(SellarBase):
    """ An OpenMDAO component to encapsulate Sellar analysis """
    def __init__(self, **kwargs):
        super(Sellar, self).__init__(**kwargs)

        self.nonlinear_solver = RecklessNonlinearBlockGS()
        self.linear_solver = ScipyKrylov()

    def setup(self):
        super(Sellar, self).setup()


class SellarFactory(SellarFactoryBase):
    """ A factory to create disciplines of Sellar analysis """
    pass

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--no-n2", action="store_false", dest='n2_view', default=True, 
                      help="display N2 openmdao viewer")
    (options, args) = parser.parse_args()

    problem = Problem()
    problem.model = Sellar()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        n2(problem)
    
