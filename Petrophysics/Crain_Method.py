import numpy as np
import numpy.typing as npt

def crain(phi: npt.ArrayLike, ff: npt.ArrayLike):
    """
    Estimate water saturation from Crain(2019)
    
    Parameters
    ----------
    bvi : int, float
        Bulk volume irreducible.
    ff : array_like
        Free fluid.    
    phi : array_like
        Porosity (must be effective).  
    sw : array_like
        Saturation of water.     
    

    Returns
    -------
    
    sw : array_like
        Water saturation from Crain equation.
    
    References
    ------------
    
    Crain E.R. (2016) Visual Analysis Rule for Water Saturation, Petrophysical Handout."""
   
    bvi = phi - ff
    sw = bvi / phi
    
    return sw
