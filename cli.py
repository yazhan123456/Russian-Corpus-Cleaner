import argparse
from cleaner.processor import clean_text

def process_file(input_path: str, output_path: str) -> None:
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    cleaned = clean_text(text)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    print(f"✅ 清洗完成！输出文件：{output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="俄语 OCR 文本清洗工具")
    parser.add_argument("input", help="原始 txt 文件路径")
    parser.add_argument("output", help="清洗后 txt 输出路径")
    args = parser.parse_args()
    process_file(args.input, args.output)
