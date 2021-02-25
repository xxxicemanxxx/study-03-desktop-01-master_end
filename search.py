import pandas as pd
import eel

### デスクトップアプリ作成課題
#step6_CSVファイルの保存先指定
def kimetsu_search(word,search_csv):
    # 検索対象取得
    df=pd.read_csv("./{}".format(search_csv))
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はいます".format(word))
        eel.monitor("『{}』はいます".format(word))
    else:
        print("『{}』はいません".format(word))
        eel.monitor("『{}』はいません".format(word))
        eel.monitor("『{}』を追加します".format(word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    #df.to_csv("./source.csv",encoding="utf_8-sig")
    df.to_csv("./{}".format(search_csv),encoding="utf_8-sig")
    print(source)
