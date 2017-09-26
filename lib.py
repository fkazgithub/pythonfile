
#時間表示のライブラリ
from datetime import datetime #datetimeをimport　
now = datetime.now() #now変数に現在の時間を入れる
print (now) #出力


#ファイル操作モジュール
import shutil #shutilをインポートする
shutil.copy("aaa.txt","bbb.txt") #aaa.txtの内容をbbb.txtにコピー

#deque,OrderedDict,defaultdict,Counter等など効率的なアルゴリズムを実装できる
from collections import Counter #collectionsからCounterをimport

count = Counter('samplesss')#countに文字列samplesssをCounterを用いて入れる
print (count)#countを出力　結果:Counter({'s': 4, 'p': 1, 'e': 1, 'm': 1, 'a': 1, 'l': 1})

dat = ["sample","apple","apple","hoge"] #datに配列として4つの文字列を代入
dat2 = dat.count("apple") # dat2にdatの配列内でappleの文字列が何個あるか数値で返す関数を入れる
print (dat2) #dat2を出力 結果:2

count_header = ["apple"] #count_headerに文字列appleを入力
result = {k:dat.count(k) for k in count_header} #resultという変数を用意しkにcounter_headerを入れていく
print (result) #resultを出力　結果:{'apple': 2}




