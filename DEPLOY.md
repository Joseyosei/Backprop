# Deploy Backprop to Vercel

Everything is in `dist/`. It is a static site: one HTML file, one logo, no build step.

## Option 1, drag and drop (30 seconds, no tooling)
1. Go to vercel.com/new
2. Drag the whole `dist` folder onto the page
3. Done. Vercel gives you a live URL.

## Option 2, CLI
```bash
npm i -g vercel
cd dist
vercel --prod
```

## Add the domain
In the Vercel project: Settings -> Domains -> Add.
Point `backprop.school` there, or buy it inside Vercel so DNS is automatic.

## Updating the course list
`courses.json` is the database. `build_data.py` regenerates it.
`site.html` has the data inlined so the site works as a single file with no fetch.
To rebuild after editing the data:
```bash
python3 build_data.py            # regenerates courses.json
python3 -c "import json,re,base64,os; \
  html=open('index.html').read(); d=json.load(open('courses.json')); \
  [c.pop('phase',None) for c in d['courses']]; \
  print('edit build step in DEPLOY.md if you change the template')"
```
