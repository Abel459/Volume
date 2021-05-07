#Import the library math to use the function pi
import math

#write a function to calcualte volume of a sphere
def vsphere(radius):
    return 4.0/3.0 * math.pi * (radius ** 3)

# a for loop to iterate from digits 1-9 and conditions for printing the results
for radius in range(1,9):
    volume = round(vsphere(radius),2)
    print('radius ' + str(radius)+ 'of a sphere is equal to the following volume of a sphere ' + str(volume))
    if volume < 25:
        print('volume is less than 25')
    elif volume > 25:
        print('Volume is greater than 25')
