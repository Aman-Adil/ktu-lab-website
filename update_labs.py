import os
import json

base_dir = r"c:\Users\amana\Networking-Lab-S6"
experiments = [
    {
        "title": "Distance Vector Routing",
        "desc": "Implementation of Distance Vector Routing algorithm in C.",
        "path": r"Distance-Vector-Routing\dvr.c"
    },
    {
        "title": "Leaky Bucket Algorithm",
        "desc": "Network traffic shaping leaky bucket implementation.",
        "path": r"Leaky-Bucket\leaky.c"
    },
    {
        "title": "Link State Routing",
        "desc": "Implementation of Link State Routing using Dijkstra.",
        "path": r"Link-State-Routing\link.c"
    },
    {
        "title": "TCP Client-Server",
        "desc": "Standard TCP socket programming server implementation.",
        "path": r"Socket-Programming\TCP\server.c"
    },
    {
        "title": "FTP Implementation",
        "desc": "File Transfer Protocol server implementation in C.",
        "path": r"File Transfer Protocol\server.c"
    },
    {
        "title": "SMTP Protocol",
        "desc": "Simple Mail Transfer Protocol client-server.",
        "path": r"SMTP\server.c"
    },
    {
        "title": "Stop and Wait",
        "desc": "Stop and wait protocol for sliding window.",
        "path": r"Sliding-Window-Protocols\Stop-N-Wait\server.c"
    },
    {
        "title": "Time Server",
        "desc": "UDP based time server implementation.",
        "path": r"Time-Server-Application\server.c"
    }
]

labs_array = "        const labs = [\n"
for i, exp in enumerate(experiments):
    full_path = os.path.join(base_dir, exp["path"])
    with open(full_path, 'r', errors='ignore') as f:
        code_str = f.read()
    
    code_escaped = json.dumps(code_str)
    
    entry = f"            {{ id: {i+1}, dept: 'CS', sem: 'S6', lang: 'language-c', title: '{exp['title']}', desc: '{exp['desc']}', code: {code_escaped} }}"
    
    if i < len(experiments) - 1:
        entry += ",\n"
    else:
        entry += "\n"
    labs_array += entry
labs_array += "        ];"

with open(r"c:\Users\amana\OneDrive\Desktop\ktu lab\new_array.txt", "w", encoding='utf-8') as f:
    f.write(labs_array)
