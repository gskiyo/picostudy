import ujson

# JSONファイルの読み込み withがあるからclose処理はいらないブロックを抜けるときに
with open('example.json', 'r') as f:
    data = ujson.load(f)

# JSONファイルの中身の表示
print(data)


# 書き込むJSONデータ
data = {'name': 'John', 'age': 25}

# JSONファイルに書き込む
with open('example.json', 'w') as f:
    ujson.dump(data, f)
