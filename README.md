# python-beautifulsoup-tw116/TW116.py ttttttttttesssssttttt

# 使用工具:
1. python
2. BeautifulSoup
3. urllib.request
4. Django.models建立的SQL tablename:tw116
5. telegram

2017/7/26 updated
# 說明:
1.使用 python beautifulsoup 4 練習爬蟲電影網站tw116.com</br>
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
*.*.判斷10個網址是否為新資料</br>
*.發送至telegram</br>

# 編輯記錄
1. 把爬蟲重複部分定義成 htmlsoup()的function
update 20170727
