import codecs
import re
import sys

with codecs.open(r"c:\Users\amana\OneDrive\Desktop\ktu lab\index.html", 'r', 'utf-8') as f:
    text = f.read()

# Replace head script
confetti_script = '<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>'
if confetti_script in text and 'papaparse' not in text:
    text = text.replace(
        confetti_script,
        confetti_script + '\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>'
    )

# Replace labs array
pattern = re.compile(r"const labs = \[.*?\n\s*\];", re.DOTALL)
match = pattern.search(text)

replacement = """let labs = [];

        async function fetchLabsData() {
            Papa.parse("https://docs.google.com/spreadsheets/d/e/2PACX-1vTapB170ZXj4vm6WcRGvmRyAYaA3tbKREgDO1lazPVE6WxRyf3chi3x4C4YeoGNeGXchwLmByJp71po/pub?output=csv", {
                download: true,
                header: true,
                skipEmptyLines: true,
                complete: function(results) {
                    labs = results.data.map(row => ({
                        ...row,
                        id: parseInt(row.id, 10)
                    }));
                    renderLabs();
                }
            });
        }"""

if match:
    print("Match found for labs array. Replacing.")
    text = text.replace(match.group(0), replacement)
else:
    print("Match NOT FOUND for labs array!")

# Replace init and render
init_call = 'initSidebar(); renderLabs();'
if init_call in text:
    text = text.replace(init_call, 'initSidebar(); fetchLabsData();')

with codecs.open(r"c:\Users\amana\OneDrive\Desktop\ktu lab\index.html", 'w', 'utf-8') as f:
    f.write(text)
print("Saved changes successfully.")
