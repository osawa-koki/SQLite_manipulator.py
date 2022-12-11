# SQLiteテスター(Python)

SQLiteをPythonで操作するためのテストプログラム。

## 環境情報

| 機能 | バージョン |
| ---- | ---- |
| Linux / Ubuntu | 22.4.* |
| Python | 3.10.* |
| SQLite | 3.34.1 |

## 環境構築手順

### Pythonインストール

Linux環境だとデフォルトでインストールされていることがほとんどだが、、、

```bash
sudo apt install python3
```

### SQLiteインストール

```bash
sudo apt install sqlite3
```

## 補足事項

executeメソッドの第二引数にはバインド機構のパラメタをタプル型で指定するが、要素が一つだけのタプル型を表すためには、「(T, )」とする必要がある。  
単に「(T)」とすると、結合優先度調整用の括弧として認識されてしまうため。  
