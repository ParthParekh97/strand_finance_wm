import os

source = '/Users/parthparekh/Desktop/StrandFinance_WM/case-study-deck/Strand Finance Case Study (Scrolling).html'
dest = '/Users/parthparekh/Desktop/StrandFinance_WM/case-study-deck/Strand Finance Case Study (Concise).html'

with open(source, 'r') as f:
    lines = f.readlines()

remove_labels = [
    "05 Research", "06 Synthesis", "07 Personas", "08 Before Journey", 
    "9 Flow", "10 AI as Material", "11 AI Augmentations",
    "16 User Flow - Step 1", "17 User Flow - Step 2", "18 User Flow - Step 3",
    "19 User Flow - Step 4", "20 User Flow - Step 5", "17 Before After"
]

skip = False
out_lines = []

for line in lines:
    if '<section data-label="' in line:
        for label in remove_labels:
            if f'data-label="{label}"' in line:
                skip = True
                break
    
    if not skip:
        out_lines.append(line)

    if skip and '</section>' in line:
        skip = False

with open(dest, 'w') as f:
    f.writelines(out_lines)

print("Concise HTML generated.")
