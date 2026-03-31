from sickle import Sickle

s = Sickle("https://api.figshare.com/v2/oai")

count = 0

for r in s.ListRecords(
    metadataPrefix="oai_cerif_openaire",
    set="portal_1148"
):
    try:
        title = r.metadata.get('title', [''])[0]
        print(title)
        count += 1

        if count == 100:
            break
    except Exception:
        continue
