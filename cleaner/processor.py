import re

def fix_hyphenated_words(text: str) -> str:
    pattern = r'([А-Яа-яЁё])- *\n? *([А-Яа-яЁё])'
    return re.sub(pattern, r'\1\2', text)

def remove_leading_fullwidth_spaces(text: str) -> str:
    return re.sub(r'^[\u3000\s]{1,3}', '', text, flags=re.MULTILINE)

def remove_law_references(text: str) -> str:
    return re.sub(r'\(ст\.\s*\d+(?:\.\d+)?\)', '', text)

def remove_number_references(text: str) -> str:
    text = re.sub(r'\(\s*п\.\s*\d+\s*ст\.\s*\d+\s*\)', '', text)
    text = re.sub(r'\(\s*стр\.\s*\d+—?\d*\s*\)', '', text)
    text = re.sub(r'\(\s*\d+\s*\)', '', text)
    text = re.sub(r'\[\s*\d+\s*\]', '', text)
    return text

def protect_section_titles(text: str) -> str:
    return re.sub(r'^(?P<title>[А-ЯЁ][А-Яа-яё\s,:–-]{3,})$', r'###\g<title>###', text, flags=re.MULTILINE)

def restore_section_titles(text: str) -> str:
    return text.replace('###', '')

def merge_broken_paragraphs(text: str) -> str:
    return re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

def clean_text(text: str) -> str:
    text = fix_hyphenated_words(text)
    text = remove_leading_fullwidth_spaces(text)
    text = protect_section_titles(text)
    text = remove_law_references(text)
    text = remove_number_references(text)
    text = merge_broken_paragraphs(text)
    text = restore_section_titles(text)
    return text
