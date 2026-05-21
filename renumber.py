import re
import sys

def renumber_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    parts = content.split('<section data-label="')
    if len(parts) <= 1:
        return
    
    total_slides = len(parts) - 1
    total_str = f"{total_slides:02d}"
    
    new_parts = [parts[0]]
    for i in range(1, len(parts)):
        part = parts[i]
        idx_str = f"{i:02d}"
        
        match = re.match(r'^([0-9\.]+\s+)?(.*?)">', part)
        if match:
            label_text = match.group(2)
            part = idx_str + " " + label_text + '">' + part[match.end():]
        
        def replace_chrome(m):
            prefix = m.group(1)
            num = m.group(2)
            sep = m.group(3)
            rest = m.group(4)
            
            if "HERO" in rest or "HERO" in sep:
                return prefix + idx_str + f" / {total_str} — HERO"
            else:
                clean_rest = re.sub(r'^[ —\-–·•\s]+', '', rest).strip()
                return prefix + idx_str + " / " + clean_rest
            
        part = re.sub(r'(<div class="chrome-tl">)([0-9\.]+(?:\s*/\s*[0-9]+)?)(\s*(?:/|—|–|-)\s*)([^<]*)', replace_chrome, part, count=1)
        
        new_parts.append(part)
        
    with open(filepath, 'w') as f:
        f.write('<section data-label="'.join(new_parts))

import os

files_to_renumber = [
    'Strand Finance Case Study.html',
    'Strand Finance Case Study (Scrolling).html',
    'Strand Finance Case Study (AI Presenter).html',
    'Strand Finance Case Study (Concise).html',
    'Strand Finance Interview deck.html',
    'Strand Finance Interview (Scrolling).html'
]

dirs = [
    '/Users/parthparekh/Desktop/StrandFinance_WM/case-study-deck',
    '/Users/parthparekh/Desktop/StrandFinance_WM/scratch/deploy_repo'
]

for d in dirs:
    for f in files_to_renumber:
        path = os.path.join(d, f)
        if os.path.exists(path):
            renumber_file(path)
            print(f"Renumbered: {path}")
