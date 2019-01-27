def timeConversion(s):
    #
    # Write your code here.
    #
    hasToBeConverted = s.find("PM")
    if hasToBeConverted == -1: 
        s = s.replace("AM", "")
        timeSplit = s.split(':')
        if timeSplit[0] == "12": timeSplit[0] = "00"
        return ':'.join(timeSplit)
    
    s = s.replace("PM", "")
    timeSplit = s.split(':')
    hourRaw = int(timeSplit[0])
    hour = hourRaw
    if hourRaw != 12: hour = hourRaw + 12
    timeSplit[0] = str(hour)
    res = ':'.join(timeSplit)
    return res

res = timeConversion("07:05:45PM") # 19:05:45
print(res)
res = timeConversion("12:00:00AM") # 00:00:00
print(res)
res = timeConversion("12:45:54PM") # 12:45:54
print(res)
res = timeConversion("12:05:39AM") # 00:05:39
print(res)