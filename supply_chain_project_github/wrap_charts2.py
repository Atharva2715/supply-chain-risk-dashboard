import re
import sys

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

count = 0
def repl(m):
    global count
    count += 1
    cid = m.group(1)
    height = m.group(2)
    if height:
        return f'<div style="position: relative; height: {height}px; width: 100%;"><canvas id="{cid}"></canvas></div>'
    else:
        return f'<div style="position: relative; height: 100%; width: 100%;"><canvas id="{cid}"></canvas></div>'

# Strip any existing wrap to prevent double wrap (if it failed before)
if '<div style="position: relative;' in text:
    print("WARNING: FOUND EXISTING WRAP. STRIPPING FIRST.")
    text = re.sub(r'<div style="position: relative; height: [0-9]+.*?px; width: 100%;"><canvas id="([a-zA-Z0-9_]+)"></canvas></div>', r'<canvas id="\1"></canvas>', text)
    text = re.sub(r'<div style="position: relative; height: 100%; width: 100%;"><canvas id="([a-zA-Z0-9_]+)"></canvas></div>', r'<canvas id="\1"></canvas>', text)

# Now wrap everything properly
pattern = re.compile(r'<canvas\s+id=[\'\"]([a-zA-Z0-9_]+)[\'\"](?:\s+height=[\'\"]([0-9]+)[\'\"])?\s*></canvas>')
new_text = pattern.sub(repl, text)

# DonutC edgecase
new_text = new_text.replace(
    '<div style="width:130px;height:130px;flex-shrink:0"><div style="position: relative; height: 100%; width: 100%;"><canvas id="donutC"></canvas></div></div>',
    '<div style="width:130px;height:130px;flex-shrink:0;position: relative;"><canvas id="donutC"></canvas></div>'
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Wrapped {count} canvases")
