""" This script contains the elements describing Gauss quadratures for numerical integration of different orders. 
That is, for different orders of quadrature the integration nodes and integration weights are defined in this script. """

import numpy as np

def GaussQuadrature(element,order):
    """ Obtain Gauss quadrature for reference element and selected quadrature order. 
        Input: - element: type of element -> 0=line, 1=tri, 2=quad 
               - order: quadrature order 
        Output: - z: Gauss nodal coordinates matrix 
                - w: Gauss integration weights """
    match element:
            case 0:  # LINE (1D ELEMENT)
                match order:
                    case 1:
                        Ng = 1
                        zg = 0
                        wg = 2
                    case 2:
                        Ng = 2
                        sq = 1/np.sqrt(3)
                        zg = np.array([[-sq], [sq]])
                        wg = np.ones([Ng])
                    case 3:
                        Ng = 3
                        sq = np.sqrt(3/5)
                        zg = np.array([[-sq], [0], [sq]])
                        wg = np.array([5/9, 8/9, 5/9])
            case 1:  # TRIANGLE
                match order:
                    case 1:
                        Ng = 1
                        zg = np.array([1/3, 1/3])
                        wg = 1/2
                    case 2:   
                        Ng = 3
                        zg = np.zeros([Ng,2])
                        #zg[0,:] = [0.5, 0.5]
                        #zg[1,:] = [0.5, 0]
                        #zg[2,:] = [0, 0.5]
                        zg[0,:] = [1/6, 2/3]
                        zg[1,:] = [1/6, 1/6]
                        zg[2,:] = [2/3, 1/6]
                        wg = np.ones(Ng)*(1/6)
                    case 24:  
                        Ng = 4  
                        zg = np.zeros([Ng,2])
                        zg[0,:] = [0.2, 0.2]
                        zg[1,:] = [0.6, 0.2]
                        zg[2,:] = [0.2, 0.6]
                        zg[3,:] = [1/3, 1/3]
                        wg = np.array([25/96, 25/96, 25/96, -27/96])
                    case 3: 
                        Ng = 6 
                        zg = np.zeros([Ng,2])
                        zg[0,:] = [0.108103018168070227360, 0.445948490915964886320]
                        zg[1,:] = [0.445948490915964886320, 0.108103018168070227360]
                        zg[2,:] = [0.445948490915964886320, 0.445948490915964886320]
                        zg[3,:] = [0.816847572980458513080, 0.091576213509770743460]
                        zg[4,:] = [0.091576213509770743460, 0.816847572980458513080]
                        zg[5,:] = [0.091576213509770743460, 0.091576213509770743460]
                        wg = np.array([0.22338158967801146570,0.22338158967801146570,0.22338158967801146570,
                                       0.10995174365532186764,0.10995174365532186764,0.10995174365532186764])*0.5          
            case 2:  # QUADRILATERAL
                match order:
                    case 1:
                        Ng = 4
                        zg = np.zeros([Ng,2])
                        sq = 1/np.sqrt(3)
                        zg[0,:] = [-sq, -sq]
                        zg[1,:] = [sq, -sq]
                        zg[2,:] = [sq, sq]
                        zg[2,:] = [-sq, sq]
                        wg = np.ones(Ng)
                    case 2:  
                        Ng = 9
                        zg = np.array([[0.774596669241483, 0.774596669241483],
                                        [0, 0.774596669241483],
                                        [-0.774596669241483, 0.774596669241483],
                                        [0.774596669241483, 0],
                                        [0, 0],
                                        [-0.774596669241483, 0],
                                        [0.774596669241483, -0.774596669241483],
                                        [0, -0.774596669241483],
                                        [-0.774596669241483, -0.774596669241483]]);
                        wg =np.array([0.308641975308641, 0.493827160493826, 0.308641975308641, 0.493827160493826, 0.790123456790123, 0.493827160493826, 0.308641975308641, 0.493827160493826, 0.308641975308641]);
                
    return zg, wg, Ng

