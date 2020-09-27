# -*- coding: utf-8 -*-
"""
  functions.py generated by WhatsOpt 1.10.4
"""
import numpy as np
from functions_base import FunctionsBase

class Functions(FunctionsBase):
    """ An OpenMDAO component to encapsulate Functions discipline """
		
    def compute(self, inputs, outputs):
        """ Functions computation """
            
        outputs['f'] = 1.0 
        outputs['g1'] = 1.0 
        outputs['g2'] = 1.0   

# WhatsOpt docking mechanism: .whatsopt_dock.yml file should contain functions entry, like
#   functions:
#     module: <python.module.name>
#     class: <ClassName>
# 
# then _impl field (= ClassName instance) is available, remove default implementation above, 
# uncomment and adapt the line below as needed
#        self._impl.compute(inputs, outputs)

# Reminder of inputs 
#   
#       inputs['x'] -> shape: 1, type: Float    
#       inputs['y1'] -> shape: 1, type: Float    
#       inputs['y2'] -> shape: 1, type: Float    
#       inputs['z'] -> shape: (2,), type: Float      
	
# To declare partial derivatives computation
# 
#    def setup(self):
#        super(Functions, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Functions """
#   
#       	partials['f', 'x'] = np.zeros((1, 1))
#       	partials['f', 'y1'] = np.zeros((1, 1))
#       	partials['f', 'y2'] = np.zeros((1, 1))
#       	partials['f', 'z'] = np.zeros((1, 2))
#       	partials['g1', 'x'] = np.zeros((1, 1))
#       	partials['g1', 'y1'] = np.zeros((1, 1))
#       	partials['g1', 'y2'] = np.zeros((1, 1))
#       	partials['g1', 'z'] = np.zeros((1, 2))
#       	partials['g2', 'x'] = np.zeros((1, 1))
#       	partials['g2', 'y1'] = np.zeros((1, 1))
#       	partials['g2', 'y2'] = np.zeros((1, 1))
#       	partials['g2', 'z'] = np.zeros((1, 2))        
