import os
import sys
import gzip
import glob
import shutil

ZIPFILES='/Users/lokeshkhandelwal/Downloads/master*.gz'

#Get file list from directory
filelist = glob.glob(ZIPFILES)

for gzfile in filelist:

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
            if lines[2] == '3' and lines[22] == '0':
                lines[22] = lines[23]
            #print("New rmngPartner: {}".format(lines[22]))
            #print(lines)
            res.append(','.join(lines))

    with gzip.open(gzfile, 'wt') as fw:
        for modified_lines in res:
            fw.write(modified_lines)

    #Move file to another location
    shutil.move(gzfile, '/Users/lokeshkhandelwal')
