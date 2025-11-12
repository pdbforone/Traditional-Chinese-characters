#!/usr/bin/env python3
"""
Generate mnemonic stories for remaining Chinese characters
"""

import re

# Tone hint mapping
tone_hints = {
    '1': ['sings', 'cheerfully', 'happily', 'high'],
    '2': ['questions', 'curiously', 'asking', 'sighing'],
    '3': ['bends down drooping', 'saying'],
    '4': ['commands', 'yells', 'sharply'],
    '5': ['says', 'neutrally']
}

def extract_tone(pinyin):
    """Extract tone number from pinyin"""
    if 'ā' in pinyin or 'ē' in pinyin or 'ī' in pinyin or 'ō' in pinyin or 'ū' in pinyin or 'ǖ' in pinyin:
        return '1'
    elif 'á' in pinyin or 'é' in pinyin or 'í' in pinyin or 'ó' in pinyin or 'ú' in pinyin or 'ǘ' in pinyin:
        return '2'
    elif 'ǎ' in pinyin or 'ě' in pinyin or 'ǐ' in pinyin or 'ǒ' in pinyin or 'ǔ' in pinyin or 'ǚ' in pinyin:
        return '3'
    elif 'à' in pinyin or 'è' in pinyin or 'ì' in pinyin or 'ò' in pinyin or 'ù' in pinyin or 'ǜ' in pinyin:
        return '4'
    else:
        return '5'  # neutral tone

def clean_pinyin(pinyin):
    """Remove tone marks from pinyin"""
    replacements = {
        'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a',
        'ē': 'e', 'é': 'e', 'ě': 'e', 'è': 'e',
        'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
        'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o',
        'ū': 'u', 'ú': 'u', 'ǔ': 'u', 'ù': 'u',
        'ǖ': 'u', 'ǘ': 'u', 'ǚ': 'u', 'ǜ': 'u'
    }
    result = pinyin
    for old, new in replacements.items():
        result = result.replace(old, new)
    return result.capitalize()

def generate_story(char, pinyin, meaning):
    """Generate a simple mnemonic story"""
    tone = extract_tone(pinyin)
    clean_py = clean_pinyin(pinyin)

    # Get tone hints
    hints = tone_hints.get(tone, tone_hints['1'])
    action = hints[0]
    emotion = hints[1] if len(hints) > 1 else ""

    if tone == '1':
        story = f"{meaning} {action} \"{clean_py}!\" {emotion}!"
    elif tone == '2':
        story = f"{meaning} {action} \"{clean_py}? Why?\" {emotion}!"
    elif tone == '3':
        story = f"{meaning} {action} {emotion} \"{clean_py}\"!"
    elif tone == '4':
        story = f"{meaning} {action} \"{clean_py}!\" {emotion}!"
    else:
        story = f"{meaning} {action} \"{clean_py}\" {emotion}!"

    return story

# Read RTH.txt and process remaining characters (1001-3039)
print("Reading RTH.txt...")
with open('/home/user/Traditional-Chinese-characters/RTH.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Output file
output_lines = []

# Process lines starting from character 1001
for i, line in enumerate(lines):
    if i < 1003:  # Skip header and first 1000 characters
        continue

    parts = line.strip().split('\t')
    if len(parts) < 9:
        continue

    try:
        char_num = parts[0]
        meaning = parts[1]
        character = parts[3]
        pinyin = parts[8]

        if not character or not pinyin or not meaning:
            continue

        tone = extract_tone(pinyin)
        clean_py = clean_pinyin(pinyin)
        story = generate_story(meaning, pinyin, meaning)

        output_line = f"{character}\t{clean_py}\t{tone}\t{meaning}\t{story}"
        output_lines.append(output_line)

    except Exception as e:
        print(f"Error processing line {i}: {e}")
        continue

# Write to file
print(f"Writing {len(output_lines)} stories...")
with open('/home/user/Traditional-Chinese-characters/remaining_stories.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"Complete! Generated {len(output_lines)} stories.")
