'''
In this bite we will look at this small server log finding the first and last system shutdown events:

INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
...
INFO 2014-07-03T23:31:22 supybot Shutdown initiated.

You need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects.
Then use datetime.timedelta to calculate the time difference between them.
'''

from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    return datetime.strptime(line.split()[1], "%Y-%m-%dT%H:%M:%S")


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_times = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            shutdown_times.append(convert_to_datetime(line))
    
    return shutdown_times[-1] - shutdown_times[0]
