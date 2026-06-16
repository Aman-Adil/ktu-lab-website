import codecs

target_file = r"c:\Users\amana\OneDrive\Desktop\ktu lab\index.html"
with codecs.open(target_file, 'r', 'utf-8') as f:
    text = f.read()

search_str = '<option value="IT" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Information Tech</option>'

replacement = """<option value="IT" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Information Tech</option>
                    <option value="EC" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Electronics (EC)</option>
                    <option value="ME" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Mechanical (ME)</option>
                    <option value="CE" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Civil (CE)</option>
                    <option value="EEE" class="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100">Electrical (EEE)</option>"""

if search_str in text:
    text = text.replace(search_str, replacement)
    with codecs.open(target_file, 'w', 'utf-8') as f:
        f.write(text)
    print("Success: Departments added.")
else:
    print("Error: Target string not found.")
