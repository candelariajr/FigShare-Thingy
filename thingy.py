from sickle import Sickle

s = Sickle("https://api.figshare.com/v2/oai")

count = 0

for r in s.ListRecords(
    metadataPrefix="oai_dc",
    set="portal_1148"
):
    try:
        md = r.metadata

        title = md.get("title", [""])[0]
        subjects = md.get("subject", [])
        resource_type = md.get("type", [])
        dates = md.get("date", [])
        descriptions = md.get("description", [])

        print("TITLE:", title)
        print("SUBJECTS:", subjects)
        print("TYPE:", resource_type)
        print("DATES:", dates)
        print("DESCRIPTION:", descriptions)
        print("-" * 40)

        count += 1
        if count == 100:
            break

    except Exception:
        continue
