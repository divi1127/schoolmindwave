import os
import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'(<div class="row gy-5">)(.*?)(?=\s*<!-- ====================== footer bottom section start ====================== -->)'

match = re.search(pattern, content, flags=re.DOTALL)
if match:
    with open('footer_original.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(0))
    print("Extracted footer.")
else:
    print("Match failed.")
