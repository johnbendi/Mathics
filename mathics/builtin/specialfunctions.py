# -*- coding: utf8 -*-

"""
Special functions
"""

import mpmath

from mathics.builtin.arithmetic import _MPMathFunction
from mathics.core.expression import Integer

class Erf(_MPMathFunction):
    """
    <dl>
    <dt>'Erf[$z$]'
        <dd>returns the error function of $z$.
    </dl>
    
    >> Erf[1.0]
     = 0.842700792949714869
    >> Erf[0]
     = 0
    >> Plot[Erf[x], {x, -2, 2}]
     = -Graphics-
    """

    mpmath_name = 'erf'
    
class ProductLog(_MPMathFunction):
    """
    <dl>
    <dt>'ProductLog[$z$]'
        <dd>returns the value of the Lambert W function at $z$.
    </dl>
    
    The defining equation:
    >> z == ProductLog[z] * E ^ ProductLog[z]
     = True
     
    Some special values:
    >> ProductLog[0]
     = 0
    >> ProductLog[E]
     = 1
     
    The graph of 'ProductLog':
    >> Plot[ProductLog[x], {x, -1/E, E}]
     = -Graphics-
    """
    
    sympy_name = 'LambertW' # function called LambertW in SymPy
    mpmath_name = 'lambertw'
    
    rules = {
        'ProductLog[0]': '0',
        'ProductLog[E]': '1',
        'ProductLog[z_] * E ^ ProductLog[z_]': 'z',
    }
    
class Zeta(_MPMathFunction):
    """
    >> Zeta[2]
     = Pi ^ 2 / 6

    >> Zeta[-2.5 + I]
     = 0.0235936105863796486 + 0.00140779960583837704 I
    """

    sympy_name = 'zeta'
    mpmath_name = 'zeta'

class BesselJ(_MPMathFunction):
    """
    >> BesselJ[0, 5.2]
     = -0.11029

    ## >> D[BesselJ[n, z], z]
    ##  = BesselJ[n - 1, z] / 2 - BesselJ[n + 1, z] / 2

    #TODO: Sympy Backend is not as powerful as Mathmeatica
    >> BesselJ[1/2, x]
     = Sqrt[2 / Pi] Sin[x] / Sqrt[x]
    """

    sympy_name = 'besselj'
    mpmath_name = 'besselj'

class Legendre(_MPMathFunction):
    def eval(self, z):
        return mpmath.legendre(1, z)
    
    def prepare_sympy(self, leaves):
        return [Integer(1)] + leaves
