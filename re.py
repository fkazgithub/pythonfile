#reライブラリ　splitの基本的な扱い

import re  #ライブラリreをimportする
str = 'a,b.c_d-e' #strに文字列a.b.c_d-eを入れる
print (str) #strの出力　結果:a,b.c_d-e

str2 = re.split('[,._-]', str) #str2にライブラリreを用いてsplitしたものを入れる
print (str2) #[,._-]でsplit(分けた)ので結果:['a', 'b', 'c', 'd', 'e']となる

print (str2[2]) #上記のsplitによって配列化したので0から数えて2番目の要素のcが出力される
