#reライブラリ　splitの基本的な扱い

import re  #ライブラリreをimportする
str = 'a,b.c_d-e' #strに文字列a.b.c_d-eを入れる
print (str) #strの出力　結果:a,b.c_d-e

str2 = re.split('[,._-]', str) #str2にライブラリreを用いてsplitしたものを入れる
print (str2) #[,._-]でsplit(分けた)ので結果:['a', 'b', 'c', 'd', 'e']となる

print (str2[2]) #上記のsplitによって配列化したので0から数えて2番目の要素のcが出力される

str3 = 'khello' #str3にkhelloと入れる
print (str3) #結果:khello
str4 = str3.strip('k') #str4にstr3からkを抜いたものを入れる()になにもいれないと空白や改行を消す
print (str4)#結果:hello

bindata = open('kokoro.txt', 'rb').read() #bindateという変数に太宰治の心のテキストを読み込ませる
text = bindata.decode('shift_jis') #shift_jisにデコード
text = re.split(r'\-{5,}',text)[2] #--------で分ける 上から[0][1][2]となる　本文は[2]なので[2]を残す 
text = re.split(r'底本：', text)[0] #フッターの底本:から区切り本文とフッターを[0]と[1]で分け本文の[0]を残す
print (text) #上記より不要なヘッダーとフッターを除いた本文のみをtextとして抽出できる