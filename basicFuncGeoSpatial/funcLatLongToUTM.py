'''
@author: T
'''
# import ffunction created in module funcDegToDec
# module needs to be in the same path
from funcDegToDec import deg_min_str_to_dec
# import utm module for convertion
# if error install utm 
import utm

def lon_lat_to_utm(lat, lon):
    ''' Function converts from any [Lat, Long] to [East, North, Grid]
    >>> lon_lat_to_utm(50.084522, -5.699057)
    ['30U 306918.367 5551517.614', 306918.367, 5551517.614]
    >>> lon_lat_to_utm('50 05.0713061 N', '005 41.9434092 W')
    ['30U 306918.379 5551517.588', 306918.379, 5551517.588]
    >>> lon_lat_to_utm(50.0845217683, -5.69905682)
    ['30U 306918.379 5551517.588', 306918.379, 5551517.588]
    
    '''
    # Convert from strings if required.
    if type(lat) == str:
        lat = deg_min_str_to_dec(lat)
    if type(lon) == str:
        long = deg_min_str_to_dec(lon)
        
    # Check if correct range    
    if not -80.0 <= lat <= 84.0:
        raise utm.OutOfRangeError('latitude out of range (must be between 80 deg S and 84 deg N)')
    if not -180.0 <= lon <= 180.0:
        raise utm.OutOfRangeError('longditude out of range (must be between 180 deg W and 180 deg E)')
    utm_pos = utm.from_latlon(lat, lon)
#    print('my utm postition from the function: {} with Lat: {} and Long: {} as input'.format(utmPos, Lat, Long))   
    # Google Earth does not accept this format. Translation for Google Earth:
    east = '%.3f' % (utm_pos[0])
    north = '%.3f' % (utm_pos[1])
    grid1 = str(utm_pos[2])
    grid2 = str(utm_pos[3])
    google_earth = (grid1 + grid2+' '+east+' '+north) 
    
    # returns Google Earth format and Easting and Northing as float
    return [google_earth, float(east), float(north)]

if __name__=="__main__":
    # prints correctly:
    print(lon_lat_to_utm(50.084522, -5.699057))
    print(lon_lat_to_utm(51.084522, -6.699057))
    # but if we mess up, it gives an error we created
    print(lon_lat_to_utm(150.084522, -5.699057))
