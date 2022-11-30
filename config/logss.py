import re
import os

lineList = []
matchPattern = re.compile(r'icloud-content.com|scarabresearch.com|internetvideoarchive.com|gov.au|appledaily.hk|wrfkjw.com|www.flickr.com|xivmodarchive.com|duba.net|wpncdn.com|archive.org|xuite.net|mastercard.com|annas-archive.org|jscsscdn.com|careerfinder.ucas.com|mitarchive.info|www.ncbi.nlm.nih.gov|tubecup.org|tigerfintech.com|espncdn.com|speedtest.net|gov.mo|contentsquare.net|Devices reach the limit|rackcdn.com|netherlandsworldwide.nl|tubecup.net|so.com|softbank.jp|visableleads.com|bittorrent.com|dspncdn.com|staticflickr.com|bose.com|fast.com|jaavnacsdw.com|edu|banking|kotobank.jp|patreon.com|commbank.com.au|pncloudfl.com|safeframe.googlesyndication.com|schengenvisainfo.com|sandai.net|gov.uk|cloudfront.net|360safe.com|cnzz.com|360.com|dbankcloud|nasa.gov|xunlei.com|miaozhen.com|qhimg.com|dbankcdn|gov.hk|imrworldwide.com|scorecardresearch.com|tumblr.com|phncdn.com|360.cn|umeng.com|onedrive.com|wikiwand.com|torrentkitty.red|openwebtorrent.com|sogou.com|btorrent.xyz|wsj.com|freexxxarchive.com|pornfilesarchive.com|compornmovsarchive.com|baidu.com|weibo.cn|weibo.com')
file = open(r'D:\pythonProject\error.log','r')
while 1:
    line = file.readline()
    if not line:
        print("Over~")
        break
    elif matchPattern.search(line):
        pass
    else:
        lineList.append(line)
file.close()
file = open(r'D:\pythonProject\error.log', 'w')
for i in lineList:
    file.write(i)
file.close()

path = r'D:\pythonProject\error.log'
os.startfile(path)