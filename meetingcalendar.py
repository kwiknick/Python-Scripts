import calendar
import time

#Show every month
for month in range (1, 13):

    #Compute the dates for each week that overlaps the month
    c = calendar.monthcalendar(2014, month)
    first_week = c[0]
    second_week = c[1]
    third_week = c[2]

    #If there is a Thursday in the first week, the second Thursday
    #is in the second week. Otherwise the second Thursday must
    #be in the third week.
    if first_week[calendar.TUESDAY]:
        meeting_date = second_week[calendar.TUESDAY]
    else:
        meeting_date = third_week[calendar.TUESDAY]

    print '%3s: %2s' % (month, meeting_date)

localTime = time.asctime(time.localtime(time.time()) )
print 'Local current time: ', localTime
