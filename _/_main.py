import json
from urllib.parse import urlparse

docs = json.load(open('_tilt_objects.json'))

for ii, doc in enumerate(docs):
    try:
        parsed_uri = urlparse(doc['meta']['url'])
        filename = '{uri.netloc}.tilt.json'.format(uri=parsed_uri)
        if filename[0] == '.':
            filename = filename[1:]
            print(filename)
        print(filename)
        with open(filename.lower()
            .replace(' ', '_')
            .replace('www.', '')
            .replace('docs', '')
            .replace('about', '')
            .replace('www2.', ''), 'w') as out:
            json.dump(doc, out, indent=2)
    except:
        print(doc['controller']['name'])
    print(ii)

