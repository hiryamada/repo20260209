# repo20260209

FastAPIを使った"hello world"を返すシンプルなAPIアプリケーション

## プロジェクト構成

```
.
├── src/
│   └── main.py          # FastAPIアプリケーション
├── tests/
│   └── test_main.py     # pytestテストコード
├── requirements.txt     # 依存パッケージ
└── README.md
```

## セットアップ

1. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

## 実行方法

開発サーバーを起動:
```bash
uvicorn src.main:app --reload
```

アプリケーションは `http://localhost:8000` で起動します。

## APIエンドポイント

- `GET /` - "hello world"メッセージを返す

レスポンス例:
```json
{
  "message": "hello world"
}
```

## テスト実行

pytestでテストを実行:
```bash
pytest
```

## API仕様

FastAPIの自動生成ドキュメント:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
