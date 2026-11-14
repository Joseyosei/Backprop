#!/usr/bin/env python3
"""Inline courses.json, universities.json and the logo into a single-file dist/index.html."""
import json, re, base64, os, pathlib

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text()
cd = json.load(open(root / "courses.json"))
for c in cd["courses"]:
    c.pop("phase", None)
un = json.load(open(root / "universities.json"))

old = '''async function boot(){
  try{
    const [r,ru]=await Promise.all([fetch("./courses.json"),fetch("./universities.json")]);
    if(!r.ok) throw new Error("HTTP "+r.status);
    D=await r.json();
    U=ru.ok ? await ru.json() : {programmes:[]};
  }catch(e){
    document.getElementById("list").innerHTML=
      '<div class="empty">Could not load the course list. Reload the page.</div>';
    return;
  }
'''
assert old in html, "bootstrap block not found in index.html; update build_site.py"
html = html.replace(old, "const DATA_BLOB=%s;\nconst UNI_BLOB=%s;\nfunction boot(){\n  D=DATA_BLOB; U=UNI_BLOB;\n"
                    % (json.dumps(cd, separators=(",", ":")), json.dumps(un, separators=(",", ":"))))

b64 = base64.b64encode((root / "logo.svg").read_bytes()).decode()
html = html.replace('src="/logo.svg"', 'src="data:image/svg+xml;base64,%s"' % b64)
html = html.replace('href="/logo.svg"', 'href="data:image/svg+xml;base64,%s"' % b64)
html = re.sub(r"\n{3,}", "\n\n", html)

os.makedirs(root / "dist", exist_ok=True)
(root / "dist" / "index.html").write_text(html)
(root / "site.html").write_text(html)
print("dist/index.html written,", len(html), "bytes")
