#Jeffrey Madrid
 #1/22/21
 #tilt sensor (bwl 328)

 from time import sleep
 print("\n")
 print("|==============================================================|")
 print("|Program displaying (x),(y),(z)-axis values in term of degrees.|")
 print("|==============================================================|")
 def convertToDegrees (positionToSplit, initialPosition, x, y, z):
    #input
    for _ in range(2):
        print("\n")
        string = input('\tEnter you value for the (x),(y),(z)-axis command 
response: ')
        positionToSplit = float(input('\tEnter where you want to split: '))
        regularStep = float(input('\tEnter the size of the regular step: '))
        initialPosition = float(input('\tEnter the initial position: '))
        x = ''
        y = ''
        z = ''
        beforeXYZ, XYZ = string[:positionToSplit], string[positionToSplit:]
        print('\nXYZ = ', XYZ)
        #proccess
        # has to be  unsigned integer(string parse to integer)
        # divide the values by 1,000, if front value is 1 * -1, if 0 stay positive
        #output
        for i in range(initialPosition, len(string), regularStep):
            if i == (initialPosition):
                x = XYZ[i:regularStep]
            if(i == regularStep):
                y = XYZ[i: i + regularStep]
            if(i == regularStep * 2):
                z = XYZ[i: regularStep * 3]
        print('\nx-axis = ' + x + ' Degrees.')
        sleep(1)
        print('\ny-axis = ' + y + ' Degrees.')
        sleep(1)
        print('\nz-axis = ' + z + ' Degrees.')
 #main function
 if __name__ == '__main__':
    repeat = 'y'
    convertToDegrees(1, 2, 3, 4, 5)
    repeat = input('\n\nWould you like to repeat? (y)es || (n)o: ')
    if repeat != 'y' and repeat != 'n':
        print('\n\tERROR: Enter (y) || (n).')
    if repeat == 'y':
        convertToDegrees(1, 2, 3, 4, 5)