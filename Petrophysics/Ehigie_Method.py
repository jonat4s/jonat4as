import numpy as np
import numpy.typing as npt

def vclay_ehigie(phit: npt.ArrayLike, phie: npt.ArrayLike):
    """Estimate the clay volume (or shale volume) from the Ehigie model.
    Parameters
    ----------
    cbw : array_like
        Clay bound water.
    phit : int, float
        Porosity total.
    phie : int, float
        Porosity effective.
         
    Returns
    -------
    vshale : array_like
        Shale Volume for the aimed interval using the Ehigie method.

    References
    ----------

    Ehigie (2010)
    """

    cbw = phit - phie
    vshale = cbw / phit


    return vclay
