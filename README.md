# python-beautifulsoup-tw116/TW116.py 

# 使用工具:
1. python
2. BeautifulSoup
3. urllib.request
4. Django.models建立的SQL tablename:tw116
5. telegram

2017/7/26 updated
# 說明:
1.使用 python beautifulsoup  4 web crawler 練習爬蟲電影網站tw116.com</br>
2.動作類電影第1頁爬取10部電影資料:</br>
  ---網址　　: /url/</br>
  ---狀態　　: 未完結、完結、連載至X集</br>
  ---上傳日期: YYYY-MM-DD</br>
  </br>
# *.判斷10個網址是否為新資料
(</br>
SELECT 網址,狀態 </br>
FROM tw116 </br>
WHERE 網址= '/url/'</br>
)  </br>
*.如果資料庫沒有相同網址，新增一筆電影資料
</br>
if SELECT.網址 == None :</br>
   INSERT 該部電影資料</br>
</br>
*.如果有該網址資料但狀態資料不同，更新該電影的狀態資料</br>
if SELECT.網址==url and SELECT.狀態!=狀態 :</br>
   UPDATE 狀態資料,內部電影內容</br>
   </br>
else  :</br>
   print('該電影不新增')</br>

</br>

# 以下為未完成項目
*.*圖片網址需要header，否則urllib2.urlretrieve抓下來會顯示 HTTP Error 403: Forbidden 錯誤。

# 編輯記錄
update 20170727</br>
1. 把爬蟲重複部分定義成 htmlsoup()的function</br>
</br>
update 20170808</br>
1. 上傳了 tw116mv_1.py、langconv.py、zh_wiki.py 三個檔案。</br>
2. 新增功能 :</br>
    (1)簡體轉為繁體內容 def simple2tradition(line) 內容有稍微修改，網路上的內容有誤，需要先轉Str.encode,再decode成('utf-8')</br>
    (2)發送telegram新增或是更新的電影內容</br>
    (3)判斷第一層頁面10個網址是否有更新連載狀態</br>
    (4)模組爬蟲定義為 def tw116_movie(tittme,typename)</br>
    (5)外層抓取資料為:上傳日期、連載狀態、電影網址、電影縮圖</br>
    (6)models.tw116.objects.filter(url__contains=網址) </br>
       相當於 select * from tw116 where url like %網址% </br>


