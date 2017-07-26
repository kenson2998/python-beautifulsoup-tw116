# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as urllib2

# 網址為動作類電影為範例
html_sample = 'http://tw116.com/vod-show-id-8.html'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
req = urllib2.Request(html_sample, headers=headers)
f = urllib2.urlopen(req)
soup = BeautifulSoup(f)

xpathx = 2
sa = {}
'''動作電影第一頁有10部電影，現在要爬出10部電影的網址'''
while xpathx < 12:
    title = '#mcon > div:nth-of-type(' + str(xpathx) + ') > dl > dt > a '

    for link in soup.select(title):
        #         print(link.get('href'))
        sa[xpathx - 1] = link.get('href')
    xpathx += 1

'''
print (sa)
sa字典顯示url
{1: '/action/quanzhanzhigedoujianghu/', 2: '/action/jueminggongjiwurenjihunduanwurenji/', 
 3: '/action/hudanlongwei/', 4: '/action/saohuang/', 5: '/action/duomingdaima/', 
 6: '/action/shijiezaiwomenjiaoxia/', 7: '/action/zhongguotuixiaoyuan/', 8: '/action/nanhaidefumie/', 
 9: '/action/chongfengzhanjingjingchang/', 10: '/action/bingfengzhongshengzhimen3Dbingfengxia/'}
'''

z = {}
g = 1
while g < 11:
    html_sample2 = 'http://tw116.com/' + sa[g]
    req2 = urllib2.Request(html_sample2, headers=headers)
    f2 = urllib2.urlopen(req2)
    soup2 = BeautifulSoup(f2)

    # for link in soup2.select('#mname'):
    #         print (link.text)
    t = 1
    while t < 8:
        for link in soup2.select('#mcon  > div:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(' + str(t) + ')'):

            if (t) == 7:
                a = str(link)
                find_cmd_head = a.find('-id-')

                find_comd_end = (a[find_cmd_head + 4:]).find('-t-1')

                find_comd_title = (a[find_cmd_head + 4:][:find_comd_end])

                html_sample3 = 'http://tw116.com/index.php?s=vod-ajaxhot-id-' + str(find_comd_title) + '-t-1'
                req3 = urllib2.Request(html_sample3, headers=headers)
                f3 = urllib2.urlopen(req3)
                soup3 = BeautifulSoup(f3)
                soup3 = (soup3.text).replace("');", '')
                soup3 = (soup3.replace("document.write('", ''))
                print (str(link.text) + soup3)
                z[t] = (str(soup3))
            else:
                print (link.text)
                z[t] = str(link.text)
        t += 1
    t = 1

    '''

    '''
    # id('mcon')/x:div[2]/x:ul[2]/x:li/x:a
    while t < 9:
        for link in soup2.select('#mcon > div:nth-of-type(2)'):
            for play in link.select('div:nth-of-type(' + str(t + 2) + ')'):
                print (play.text)

            for playurl in link.select('ul:nth-of-type(' + str(t + 1) + ') > li > a'):
                print (str(playurl.text))
                z[8] = str(playurl.text)
        t = t + 1
    g = g + 1
    # for describe in soup2.select('#mcon > div:nth-of-type(2) > div:nth-of-type(6)'):
    #     print (describe.text)
#     models.tw116.objects.create(
#             moviename=z[1],
#             state=z[2],
#             actor=z[3],
#             typea=z[4],
#             language=z[5],
#             up_date=z[6] ,
#             describe=describe,
#             url=html_sample2,
#             popularity=z[7],

#         )
