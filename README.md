# 🇷🇺 ru-corpus-cleaner

A Python toolkit for cleaning Russian scanned book text (OCR) from Z-Library or similar sources, designed for building NLP-ready corpora.

一个用于清洗俄语图书扫描文本的 Python 工具，适合预处理后用于自然语言处理模型训练。

## ✅ Features 功能

- ✅ Restore broken words like `го-\nрод` → `город`
- ✅ Remove legal references `(ст. 35)` / page refs `(стр. 120)`
- ✅ Delete citation marks `[15]`, `(120)`
- ✅ Detect and protect headings while merging broken paragraphs
- ✅ 全角空格清除、断词修复、编号剔除、段落还原

## 📦 Usage 用法

```bash
python cli.py examples/sample_raw.txt examples/sample_cleaned.txt
```

## 📁 Directory Structure 项目结构

- `cli.py`: CLI interface
- `cleaner/processor.py`: all text processing functions
- `examples/`: input/output demo

## 🧠 Why it's useful?

This helps researchers and NLP developers extract clean text from scanned Russian documents, useful for:
- Language modeling
- Topic modeling
- Corpus analysis
