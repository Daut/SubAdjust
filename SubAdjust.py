import re


def subadjust(filename, secOffset, milisecOffset):
    f = open(filename, 'r')
    newFile = open(filename.split('.')[0]+'New'+'.srt', 'w+')
    lines = f.readlines()
    for line in lines:
        if re.match('[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}', line):
            startTime, endTime = line.split('-->')
            hrsStart, minsStart, secsStart = startTime.split(':')
            hrsEnd, minsEnd, secsEnd = endTime.split(':')
            secsStart, milisecsStart = secsStart.split(',')
            milisecsStart = milisecsStart[:-1]
            secsEnd, milisecsEnd = secsEnd.split(',')
            milisecsEnd = milisecsEnd[:-1]

            secsStart = int(secsStart) + secOffset
            milisecsStart = int(milisecsStart) + milisecOffset
            if milisecsStart >= 1000:
                secsStart = secsStart + milisecsStart/1000
                milisecsStart = milisecsStart % 1000
            if secsStart >= 60:
                minsStart = int(minsStart) + secsStart/60
                secsStart = secsStart % 60

            secsEnd = int(secsEnd) + secOffset
            milisecsEnd = int(milisecsEnd) + milisecOffset
            if milisecsEnd >= 1000:
                secsEnd = secsEnd + milisecsEnd/1000
                milisecsEnd = milisecsEnd % 1000
            if secsEnd >= 60:
                minsEnd = int(minsEnd) + secsEnd/60
                secsEnd = secsEnd % 60

            newLine = hrsStart+':'+str(minsStart)+':'+str(secsStart)+','+str(milisecsStart)+' -->'+hrsEnd+':'+str(minsEnd)+':'+str(secsEnd)+','+str(milisecsEnd)+'\n'
            newFile.write(newLine)
        else:
            newFile.write(line)
    f.close()
    newFile.close()


filename = raw_input('Please insert full path of the .srt file: ')
secOffset = int(raw_input('Please insert number of seconds that you want subtitle to move: '))
milisecOffset = int(raw_input('Please insert number of miliseconds that you want subtitle to move: '))
subadjust(filename, secOffset, milisecOffset)
