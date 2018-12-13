
# Using 24-hour time as parameter to method 
# Returns the time in words, using 12-hour format followed by am or pm.
def talk(time):
    splitHour, splitMinute = time.split(':')
    hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', 
    '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    hourWords = [' twelve ', ' one ', ' two ', ' three ', ' four ', ' five ', ' six ', ' seven ', ' eight ',
    ' nine ', ' ten ', ' eleven ']
    hourWords += hourWords
    minuteTens = ['0', '1', '2', '3', '4', '5']
    minuteTensWords = ['oh ', ' ', 'twenty ', 'thirty ', 'fourty ', 'fifty ']
    minuteOnes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
    '14', '15', '16', '17', '18', '19']
    minuteOnesWords = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 
    'ten ', 'eleven ', 'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 
    'eighteen ', 'nineteen ']

    hourDict = dict(zip(hours, hourWords))
    minuteTensDict = dict(zip(minuteTens, minuteTensWords))
    minuteOnesDict = dict(zip(minuteOnes, minuteOnesWords))

    # String formatting 
    noon = 'AM' if int(splitHour) < 12 else 'PM'
    #Remove 'oh' from dict if minutes are 00
    if splitMinute == '00': 
        minuteTensDict['0'] = '' 
    
    # Use ten-nineteen
    if int(splitMinute) > 9 and int(splitMinute) < 20:
        return print(
            f'It\'s{hourDict.get(splitHour)}' +
            f'{minuteOnesDict.get(splitMinute)}{noon}')
    else:
        return print(
            f'It\'s{hourDict.get(splitHour)}' +
            f'{minuteTensDict.get(splitMinute[0])}' +
            f'{minuteOnesDict.get(splitMinute[1])}{noon}')

talk('00:00')
talk('01:30')
talk('12:05')
talk('14:01')
talk('20:29')
talk('21:00')
talk('23:11')