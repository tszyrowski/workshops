'''
Created on 16 Jul 2017

@author: T
'''
import math 

def calc_distance(utm_pos_1, utm_pos_2):
    ''' Easier to read function to calculate the line distance between two points.
    
    :param arg1: Easting and Northing of the first position
    :param arg2: Easting and Northing of the second position
    :type arg1: tuple (Easting, Northing)
    :type arg1: tuple (Easting, Northing)
    :return: return distance in metres
    :rtype: float
    '''
    try:
        # x,y coordinates of the first point
        x_1 = utm_pos_1[0]
        y_1 = utm_pos_1[1]
        # x,y coordinates of the second point
        x_2 = utm_pos_2[0]
        y_2 = utm_pos_2[1]
        # cartesian distance
        distance = math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2)
        
        return distance  
          
    except Exception as e: print('Check if coordinates in correct form as Easting, Northing)\n becasue: {}'.format(e))

if __name__=="__main__":
    
    utm1 = [306918.367, 5551517.614]
    utm2 = [661153.63, 5661742.488]
    dist = calc_distance(utm1, utm2)
    print("the distance is {} km".format(dist/1000))