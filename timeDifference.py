# timeDifference.py
# Written By: Matthew Talamantes
# Date: December 31, 2019
# A basic app to return the number of hours between provided times.  

from datetime import datetime

def convertTo24(time):
    """Converts time to 24 hour representation."""

    time = time.lower()
    if time[-2::] == 'pm':
        if time[0:time.find(':'):] != '12':
            colonIndex = time.find(':')
            timeInt = int(time[0:colonIndex:])
            timeInt += 12
            timeInt = str(timeInt)
            time = timeInt + time[colonIndex:-2:]
        else:
            time = time[0:-2:]
    else:
        if time[-2:time.find(':'):] != 12:
            time = time[0:-2:]
        else:
            time = '0' + time[time.find(':'):-2:]
    
    return time

def validateInput(timeString):
    '''Validates user imput, ensuring it only contains times, 
    printing message to console and returning False if something isn't right.
    If it is valid it returns a list containing a list of the [start-time, end-time] pairs between commas.'''
    
    if timeString == '':
        print('You must imput some times!')
        return False
    
    timeString = timeString.lower()
    acceptableChars = 'amp1234567890:,- '
    for char in timeString:
        if char not in acceptableChars:
            print('Unknown character used!')
            return False
    
    timeString = timeString.replace(' ', '')
    timeArray = timeString.split(',')
    if timeArray[-1] == '':
        timeArray.pop(-1)
    
    # Seperate the beginning time from the end time.
    timeFrameList = []
    for item in timeArray:
        if '-' not in item:
            print('End time not specified! Seperate end time from beginning time with a "-".')
            return False
        itemList = item.split('-')

        # Check if minutes included, if not set to #:00.
        timeIndex = 0
        for time in itemList:
            if ':' not in time:
                
                if time[-2::] == 'pm' or time[-2::] == 'am':
                    if int(time[0:-2:]) > 12:
                        print('Invalid time given, did you forget the colon?')
                        return False
                    time = time[0:-2:] + ':00' + time[-2::]
                else:
                    time = time + ':00'
            
            # Convert to 24 hour time if not already.
            if time[-2::] == 'pm' or time[-2::] == 'am':
                time = convertTo24(time)
            
            itemList[timeIndex] = time
            timeIndex += 1

        # TO-DO: Check if end time is on the next day and return error if it is until I implement the ability to handle it.

        timeFrameList.append(itemList)

    return timeFrameList


def timeDiffCalc(timeList):
    """Calculate the hours between the time sets in timeList."""
    
    hourCount = 0.0
    # Since the date is irrelevant for our puroses use the current date so that we can create a datetime object.
    todaysDateObject = datetime.now()
    todaysMonth = todaysDateObject.month
    todaysYear = todaysDateObject.year
    
    for timeSet in timeList:

        todaysDay = todaysDateObject.day
        # TO-DO: Convert times to minute representations and subtract the start time from the end time so I don't have to deal with the datetime mess.

        # Check if the end date ends on the next date.
        startTime = timeSet[0]
        endTime = timeSet[1]
        startHour = int(startTime[0:startTime.find(':'):])
        endHour = int(endTime[0:endTime.find(':'):])
        if endHour < startHour:
            todaysDay += 1


        # Set each time set to time objects. 
        timeObjectList = []
        for item in timeSet:
            colonIndex = item.find(':')
            itemHour = int(item[0:colonIndex:])
            itemMinute = int(item[colonIndex + 1::])
            timeObject = datetime(todaysYear, todaysMonth, todaysDay, itemHour, itemMinute)
            timeObjectList.append(timeObject)
        
        # Get the hour difference between the two datetime objects
        secondDifference = timeObjectList[1] - timeObjectList[0]
        hoursDifference = (secondDifference.seconds / 60) / 60
        hourCount += hoursDifference
    
    return hourCount
        



def main():
    '''The main code for the program.'''
    
    # Input and validation loop
    validInput = False
    while not validInput:
        timeString = input('Enter the times to get the hours of. E.g. 1:40PM-2:23PM, 10:52AM-4:14PM: ')
        timeArray = validateInput(timeString)
        if type(timeArray) == list:
            validInput = True
        else:
            continue
    
    hours = timeDiffCalc(timeArray)
    print(hours)
    # TO-DO: 


if __name__ == '__main__':
    main()