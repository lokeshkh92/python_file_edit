import os
import sys
import gzip
import glob
import shutil
from datetime import datetime as dt
import pytz
import datetime

#Get epoch to be replaced
tz = pytz.timezone('Australia/Sydney')
timestamp = datetime.datetime(2020, 4, 5, 0, 45).strftime('%s')
#Get file list from directory
ZIPFILES='/DiskPCap/roamware2/VHA_DL_TESTING/master*.gz'
filelist = glob.glob(ZIPFILES)

for gzfile in filelist:
    timestamp = int(timestamp) + 900
    dt1 = dt.fromtimestamp(int(timestamp), tz)
    recordtime = dt1.strftime('%Y-%m-%d %H:%M:%S')
    timestampfinal = timestamp * 1000
    res = []
    with gzip.open(gzfile, 'rt') as fr:
        for line in fr:
            #print(line)
            lines = line.split(',')
            #RecordTime = lines[0]
            #rmngPartnerNWId = lines[22]
            #partnerNWId = lines[23]
            #print("RecordTime: {}".format(RecordTime))
            #print("Original rmngPartner: {}".format(rmngPartnerNWId))
            #print("Original Partner: {}".format(partnerNWId))
            #Copy value of column#23 to column#22
            #if lines[2] == '3' and lines[22] == '0':
            #    lines[22] = lines[23]
            #print("New rmngPartner: {}".format(lines[22]))
	    lines[0] = str(recordtime) 
	    lines[5] = str(timestampfinal)
	    lines[6] = str(timestampfinal)
            #print(lines)
            res.append(','.join(lines))

    with gzip.open(gzfile, 'wt') as fw:
        for modified_lines in res:
            fw.write(modified_lines)

    #Move file to another location
    shutil.move(gzfile, '/DiskPCap/roamware2/VHA_DL_TESTING/timechanged')
