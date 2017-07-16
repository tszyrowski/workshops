'''
@author: T
'''
def calc_distance_short(utm_pos_1, utm_pos_2):
    ''' Calculate straight line distance between two points: works 
    but is difficult to read!'''
    return ((utm_pos_1[0]-utm_pos_2[0])**2+(utm_pos_1[1]-utm_pos_2[1])**2)**(0.5)

