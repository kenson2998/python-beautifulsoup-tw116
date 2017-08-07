# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/wonderful/workspace/wonderful/kensontest2')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'kensontest2.settings'

import django
# if django.VERSION >= (1, 7):  # 自动判断版本
django.setup()

from bs4 import BeautifulSoup
import urllib.request as urllib2
from appkenson import models
import time
import datetime
from langconv import *


def simple2tradition(line):
    # 将简体转换成繁体
    line = line.encode('utf-8')

    line = Converter('zh-hant').convert(line.decode('utf-8'))
    return line

def tw116_movie(tittme,typename):
    import telegram
    bot = telegram.Bot(token='276144825:AAGetdwa5-9gbuguHpQsDrllQH8uIbHKkEM')
    while tittme < 7:

        # 網址為卡通類電影為範例
        if tittme == 1 :
            html_sample = 'http://tw116.com/vod-show-id-'+typename+'.html'
        else:
            html_sample = 'http://tw116.com/vod-show-id-'+typename+'-p-' + str(tittme) + '.html'

        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        req = urllib2.Request(html_sample, headers=headers)
        f = urllib2.urlopen(req)
        soup = BeautifulSoup(f)

        xpathx = 1
        sa = {}
        sa1 = {}
        sa2 = {}
        sa3 = {}
        aaa = {}

        # 電影第一頁有10部電影，現在要爬出10部電影的網址


        while xpathx < 11:
            title = '#mcon > div:nth-of-type(' + str(xpathx + 1) + ') > dl > dt > a '
            update_mdate = '#mcon > div:nth-of-type(' + str(xpathx + 1) + ') > dl > dd:nth-of-type(4) '
            update_status = '#mcon > div:nth-of-type(' + str(xpathx + 1) + ') > dl > dd:nth-of-type(2) '
            img = '#mcon > div:nth-of-type(' + str(xpathx + 1) + ') > a > img '

            for link in soup.select(update_mdate):
                sa1[xpathx] = link.text
            for link in soup.select(update_status):
                sa2[xpathx] = sa1[xpathx], link.text
            for link in soup.select(title):
                sa3[xpathx] = sa1[xpathx][0], sa2[xpathx][1], link.get('href'), link.text
            for link in soup.select(img):
                sa[xpathx] = sa1[xpathx], sa2[xpathx][1], sa3[xpathx][2], sa3[xpathx][3], link.get('src')


            xpathx += 1

        # print (sa)

        '''sa字典顯示url 0,1,2,3,4
        {1: ('updatetime', 'status', 'url', 'moviename', 'imgurl'),
         2: ('上传：2017-08-03', '状态：完结BD', '/war/shengsizhiqiang/', '生死之墙', '/Upload/2017-08/5982eec931ede.jpg'),..}
        '''
        g = 1
        v = 1
        while g < len(sa):

            filter_url=models.tw116.objects.filter(url__contains=sa[g][2])#select * where url like %sa[g][2]%

            if len(filter_url) > 0:

                if len(filter_url.filter(state__exact=sa[g][1])) == 0: # 如果第一次撈的資料中 where ='sa[g][1]'找不到相同的值，代表更新連載欄位的值
                    # print('update...' + sa[g][2] + sa[g][0] + sa[g][1])
                    filter_url.update(up_date=sa[g][0],state=sa[g][1])
                    contentphoto = "更新電影的資料:" + sa[g][3] + '\n\n' + sa[g][1] + '\n網址:\n' + 'http://tw116.com' + \
                                   sa[g][2]
                    bot.sendMessage(chat_id='-1001093273464', text=simple2tradition(contentphoto))
                    # urllib2.urlretrieve('http://tw116.com' + str(sa[g][4]), "1.jpg")

                    # photo = open('1.png', 'rb')

                    # bot.sendPhoto(chat_id='-1001093273464', photo=photo,caption=contentphoto , reply_to_message_id="0")
                    # photo.close()
            else:
                aaa[v] = sa[g][2]
                v += 1
            g += 1
        # print (aaa)

        if aaa != {}:

            z = {}
            g = 1
            while g <= len(aaa):
                html_sample2 = 'http://tw116.com' + aaa[g]
                req2 = urllib2.Request(html_sample2, headers=headers)
                f2 = urllib2.urlopen(req2)
                soup2 = BeautifulSoup(f2)

                # for link in soup2.select('#mname'):
                #         print (link.text)
                t = 1
                while t < 8:
                    for link in soup2.select(
                                            '#mcon  > div:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(' + str(
                                        t) + ')'):

                        if (t) == 7:
                            a = str(link)
                            find_cmd_head = a.find('-id-')

                            find_comd_end = (a[find_cmd_head + 4:]).find('-t-1')

                            find_comd_title = (a[find_cmd_head + 4:][:find_comd_end])

                            html_sample3 = 'http://tw116.com/index.php?s=vod-ajaxhot-id-' + str(
                                find_comd_title) + '-t-1'
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

                # id('mcon')/x:div[2]/x:ul[2]/x:li/x:a
                describe = ''
                liveurl = ''
                mvtype = ''
                while t < 11:

                    for link in soup2.select('#mcon > div:nth-of-type(2)'):

                        for play in link.select('div:nth-of-type(' + str(t + 2) + ')'):
                            mv_title = (z[1].replace('片　　名：', ''))[:2]
                            if (play.text).find('剧情介绍') > 0 and (play.text).find(mv_title) > 0:
                                describe = (play.text)
                                z[9] = describe
                            if (play.text).find('facebook评论') < 0 and (play.text).find('剧情介绍') < 0 and len(play.text) > 0:

                                mvtype = mvtype + (play.text)
                                z[10] = mvtype.replace('影片来源：', ' ')

                        for playurl in link.select('ul:nth-of-type(' + str(t + 1) + ') > li > a'):

                            if len(playurl.text) > 0:
                                liveurl = liveurl + ' ' + (playurl.text)

                            z[8] = liveurl

                    liveurl = liveurl + '\n'
                    t = t + 1
                    z[6] = sa[g][0]
                    z[2] = sa[g][1]

                g = g + 1

                # for describe in soup2.select('#mcon > div:nth-of-type(2) > div:nth-of-type(6)'):
                #     print (describe.text)
                time.sleep(5)

                contentphoto = "新增了電影:" + z[1].replace('　　', '') + "\n" +z[9][:300]+'...' + '\n\n網址:\n'+html_sample2

                # urllib2.urlretrieve('http://tw116.com' + str(sa[g][4]), "1.jpg")

                # photo = open('1.png', 'rb')
                # bot.sendPhoto(chat_id='-1001093273464', photo=photo, caption=contentphoto, reply_to_message_id="0")


                bot.sendMessage(chat_id='-1001093273464', text=simple2tradition(contentphoto))
                # photo.close()
                models.tw116.objects.create(
                    moviename=z[1].replace('　　', ''),
                    state=z[2],
                    actor=z[3].replace('　　', ''),
                    typea=z[4].replace('　　', ''),
                    language=z[5].replace('　　', ''),
                    up_date=z[6],
                    describe=z[9][:123]+'...',
                    url=html_sample2,
                    Popularity=z[7],
                    mv_source=z[8],
                    # source_type=z[10],
                    update_date=datetime.datetime.now(),
                    # .strftime("%Y-%m-%d %H:%M")
                )

        else:
            print ('page'+str(tittme)+',data is existed')
        tittme += 1


if __name__ == '__main__':

    try:
        while True:
            tw116_movie(1, '8')  #動作
            tw116_movie(1,'11')  #科幻
            tw116_movie(1,'9')   #喜劇
            tw116_movie(1,'10')  #愛情
            tw116_movie(1,'23')  #劇情
            tw116_movie(1,'13')  #戰爭
            tw116_movie(1,'3')   #卡通
            tw116_movie(1,'4')   #綜藝
            tw116_movie(1, '17') #歐美
            print ('waiting 3600s')
            time.sleep(3600)
    except BaseException as ass:
        print(ass)

