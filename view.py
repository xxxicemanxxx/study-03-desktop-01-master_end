import eel
import desktop
import search

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
#step6_CSVファイルの保存先指定
def kimetsu_search(word,search_csv):
    search.kimetsu_search(word,search_csv)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)