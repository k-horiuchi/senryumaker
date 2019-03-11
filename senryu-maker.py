import itertools
hiragana = ('あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','ら','り','る','れ','ろ','わ','を','ん')
for v in itertools.product(hiragana , repeat = 17): # ひらがなタプルから17個要素を使う組み合わせをタプル型で出力
  v = list(v) # タプル型をリスト型にキャスト
  v.insert (5,'　') # 空白文字を追加。無くても良い
  v.insert(13,'　') # 空白文字を追加。無くても良い
  print(''.join(v)) # リスト型を文字列型にキャスト
