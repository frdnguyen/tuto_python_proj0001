#%%

def PolarToCartesian(rho,theta):
    """
    Parameters
    ----------
    rho : rayon
        
    theta : angle en dégrés
        

    Returns
    -------
    Coordonnées cartésiennces d'un point défini  à partir de ses coordonnées polaires.

    """
    import math
    theta = theta * math.pi/180
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x,y
