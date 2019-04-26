# -*- coding: utf-8 -*-
"""
  constraints.py generated by WhatsOpt. 
"""
import numpy as np
from constraints_base import ConstraintsBase

class Constraints(ConstraintsBase):
    """ An OpenMDAO component to encapsulate Constraints discipline """	
    
    def __init__(self, scalers):
        super(Constraints, self).__init__()
        self.scalers=scalers
		
    def compute(self, inputs, outputs):
        """ Constraints computation """
        ESF = inputs['ESF']*self.scalers['ESF']
        outputs['con1_esf'] = ESF - 1.5
        outputs['con2_esf'] = 0.5 - ESF  
        
        outputs['con_dpdx'] = inputs['dpdx']*self.scalers['dpdx'] - 1.04
        outputs['con_temp'] = inputs['Temp']*self.scalers['Temp']- 1.02 
        outputs['con_theta_low'] = 0.96-inputs['Theta']*self.scalers['Theta']
        outputs['con_theta_up'] = inputs['Theta']*self.scalers['Theta']-1.04
        outputs['con_dt'] = inputs['DT']*self.scalers['DT']        
        outputs['con_sigma1'] = inputs['sigma'][0]*self.scalers['sigma'][0]-1.09
        outputs['con_sigma2'] = inputs['sigma'][1]*self.scalers['sigma'][1]-1.09
        outputs['con_sigma3'] = inputs['sigma'][2]*self.scalers['sigma'][2]-1.09 
        outputs['con_sigma4'] = inputs['sigma'][3]*self.scalers['sigma'][3]-1.09 
        outputs['con_sigma5'] = inputs['sigma'][4]*self.scalers['sigma'][4]-1.09 
   

# Reminder: inputs of compute()
#   
#       inputs['DT'] -> shape: (1,), type: Float    
#       inputs['ESF'] -> shape: (1,), type: Float    
#       inputs['Temp'] -> shape: (1,), type: Float    
#       inputs['Theta'] -> shape: (1,), type: Float    
#       inputs['dpdx'] -> shape: (1,), type: Float    
#       inputs['sigma'] -> shape: (5,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Constraints, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Constraints """
#   
#       	partials['con1_esf', 'DT'] = np.zeros((1, 1))
#       	partials['con1_esf', 'ESF'] = np.zeros((1, 1))
#       	partials['con1_esf', 'Temp'] = np.zeros((1, 1))
#       	partials['con1_esf', 'Theta'] = np.zeros((1, 1))
#       	partials['con1_esf', 'dpdx'] = np.zeros((1, 1))
#       	partials['con1_esf', 'sigma'] = np.zeros((1, 5))
#       	partials['con2_esf', 'DT'] = np.zeros((1, 1))
#       	partials['con2_esf', 'ESF'] = np.zeros((1, 1))
#       	partials['con2_esf', 'Temp'] = np.zeros((1, 1))
#       	partials['con2_esf', 'Theta'] = np.zeros((1, 1))
#       	partials['con2_esf', 'dpdx'] = np.zeros((1, 1))
#       	partials['con2_esf', 'sigma'] = np.zeros((1, 5))
#       	partials['con_dpdx', 'DT'] = np.zeros((1, 1))
#       	partials['con_dpdx', 'ESF'] = np.zeros((1, 1))
#       	partials['con_dpdx', 'Temp'] = np.zeros((1, 1))
#       	partials['con_dpdx', 'Theta'] = np.zeros((1, 1))
#       	partials['con_dpdx', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_dpdx', 'sigma'] = np.zeros((1, 5))
#       	partials['con_dt', 'DT'] = np.zeros((1, 1))
#       	partials['con_dt', 'ESF'] = np.zeros((1, 1))
#       	partials['con_dt', 'Temp'] = np.zeros((1, 1))
#       	partials['con_dt', 'Theta'] = np.zeros((1, 1))
#       	partials['con_dt', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_dt', 'sigma'] = np.zeros((1, 5))
#       	partials['con_sigma1', 'DT'] = np.zeros((1, 1))
#       	partials['con_sigma1', 'ESF'] = np.zeros((1, 1))
#       	partials['con_sigma1', 'Temp'] = np.zeros((1, 1))
#       	partials['con_sigma1', 'Theta'] = np.zeros((1, 1))
#       	partials['con_sigma1', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_sigma1', 'sigma'] = np.zeros((1, 5))
#       	partials['con_sigma2', 'DT'] = np.zeros((1, 1))
#       	partials['con_sigma2', 'ESF'] = np.zeros((1, 1))
#       	partials['con_sigma2', 'Temp'] = np.zeros((1, 1))
#       	partials['con_sigma2', 'Theta'] = np.zeros((1, 1))
#       	partials['con_sigma2', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_sigma2', 'sigma'] = np.zeros((1, 5))
#       	partials['con_sigma3', 'DT'] = np.zeros((1, 1))
#       	partials['con_sigma3', 'ESF'] = np.zeros((1, 1))
#       	partials['con_sigma3', 'Temp'] = np.zeros((1, 1))
#       	partials['con_sigma3', 'Theta'] = np.zeros((1, 1))
#       	partials['con_sigma3', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_sigma3', 'sigma'] = np.zeros((1, 5))
#       	partials['con_sigma4', 'DT'] = np.zeros((1, 1))
#       	partials['con_sigma4', 'ESF'] = np.zeros((1, 1))
#       	partials['con_sigma4', 'Temp'] = np.zeros((1, 1))
#       	partials['con_sigma4', 'Theta'] = np.zeros((1, 1))
#       	partials['con_sigma4', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_sigma4', 'sigma'] = np.zeros((1, 5))
#       	partials['con_sigma5', 'DT'] = np.zeros((1, 1))
#       	partials['con_sigma5', 'ESF'] = np.zeros((1, 1))
#       	partials['con_sigma5', 'Temp'] = np.zeros((1, 1))
#       	partials['con_sigma5', 'Theta'] = np.zeros((1, 1))
#       	partials['con_sigma5', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_sigma5', 'sigma'] = np.zeros((1, 5))
#       	partials['con_temp', 'DT'] = np.zeros((1, 1))
#       	partials['con_temp', 'ESF'] = np.zeros((1, 1))
#       	partials['con_temp', 'Temp'] = np.zeros((1, 1))
#       	partials['con_temp', 'Theta'] = np.zeros((1, 1))
#       	partials['con_temp', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_temp', 'sigma'] = np.zeros((1, 5))
#       	partials['con_theta_low', 'DT'] = np.zeros((1, 1))
#       	partials['con_theta_low', 'ESF'] = np.zeros((1, 1))
#       	partials['con_theta_low', 'Temp'] = np.zeros((1, 1))
#       	partials['con_theta_low', 'Theta'] = np.zeros((1, 1))
#       	partials['con_theta_low', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_theta_low', 'sigma'] = np.zeros((1, 5))
#       	partials['con_theta_up', 'DT'] = np.zeros((1, 1))
#       	partials['con_theta_up', 'ESF'] = np.zeros((1, 1))
#       	partials['con_theta_up', 'Temp'] = np.zeros((1, 1))
#       	partials['con_theta_up', 'Theta'] = np.zeros((1, 1))
#       	partials['con_theta_up', 'dpdx'] = np.zeros((1, 1))
#       	partials['con_theta_up', 'sigma'] = np.zeros((1, 5))        
