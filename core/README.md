# ai-review-kit

AI生成コードのレビュー観点を自動化するツールの試作。

## 現状

型定義とCI基盤まで実装済み。ルール実装の前段で開発を停止している。

- `core/`: `Finding` / `Severity` / `Rule` の型定義
- CI: ruff + mypy (strict) + pytest を GitHub Actions で実行

## 停止した理由

PMOとしての実務に直結するツール（Slack × Google Workspace の業務自動化）を
優先したため。本リポジトリの設計方針とCI構成はそちらに引き継いでいる。

## 設計メモ

- `Finding` は pydantic モデル（JSON化を前提とし、MCPサーバー側での再利用を想定）
- `Severity` は StrEnum（ルール一覧の列挙を想定）
- `Rule` は ABC（実装漏れを型で防ぐ）