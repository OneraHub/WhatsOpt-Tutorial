# -*- coding: utf-8 -*-
"""
  disc2.py generated by WhatsOpt 1.10.4
"""
import numpy as np
from sellar.disc2_base import Disc2Base

class Disc2(Disc2Base):
    """ An OpenMDAO component to encapsulate Disc2 discipline """
		
    def compute(self, inputs, outputs):
        """ Disc2 computation """
            
        outputs['y2'] = 1.0   

# WhatsOpt docking mechanism: .whatsopt_dock.yml file should contain disc2 entry, like
#   disc2:
#     module: <python.module.name>
#     class: <ClassName>
# 
# then _impl field (= ClassName instance) is available, remove default implementation above, 
# uncomment and adapt the line below as needed
#        self._impl.compute(inputs, outputs)

# Reminder of inputs 
#   
#       inputs['y1'] -> shape: 1, type: Float    
#       inputs['z'] -> shape: (2,), type: Float      
	
# To declare partial derivatives computation
# 
#    def setup(self):
#        super(Disc2, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Disc2 """
#   
#       	partials['y2', 'y1'] = np.zeros((1, 1))
#       	partials['y2', 'z'] = np.zeros((1, 2))        
