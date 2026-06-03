import csv
import requests
from sickle import Sickle

LIMIT = 100
OAI_URL = "https://api.figshare.com/v2/oai"
OUTPUT_CSV = "figshare_theses_test.csv"

FIELDS = [
    "Title",
    "Creator",
    "Keywords",
    "Description",
    "DOI",
    "Year Created",
    "Program of Study",
    "Department",
    "Advisor",
    "College or School",
    "Language",
    "Dissertation or Thesis Type"
]


def first(md, key):
    return md.get(key, [""])[0] if md.get(key) else ""


def joined(md, key):
    return "; ".join(md.get(key, []))


def get_doi_from_cerif(record):
    doi_el = record.xml.find(".//{*}DOI")

    if doi_el is not None and doi_el.text:
        doi = doi_el.text.strip().rsplit(".v", 1)[0]
        return f"https://doi.org/{doi}"

    return ""


def get_figshare_fields_from_doi(doi_url):
    extra = {
        "Program of Study": "",
        "Department": "",
        "Advisor": "",
        "College or School": ""
    }

    if not doi_url:
        return extra

    try:
        article_id = doi_url.rstrip("/").split(".")[-1]
        api_url = f"https://api.figshare.com/v2/articles/{article_id}"

        r = requests.get(api_url, timeout=20)
        r.raise_for_status()

        data = r.json()

        for field in data.get("custom_fields", []):
            name = field.get("name", "").strip()
            value = field.get("value", "")

            if isinstance(value, list):
                value = "; ".join(str(v) for v in value)

            if name in extra:
                extra[name] = str(value).strip()

    except Exception as e:
        print(f"Error getting Figshare API data for {doi_url}: {e}")

    return extra


s = Sickle(OAI_URL)

dc_records = s.ListRecords(
    metadataPrefix="oai_dc",
    set="portal_1148"
)

cerif_records = s.ListRecords(
    metadataPrefix="oai_cerif_openaire",
    set="portal_1148"
)

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()

    count = 0

    for dc_record, cerif_record in zip(dc_records, cerif_records):
        md = dc_record.metadata

        doi_url = get_doi_from_cerif(cerif_record)
        extra = get_figshare_fields_from_doi(doi_url)

        row = {
            "Title": first(md, "title"),
            "Creator": joined(md, "creator"),
            "Keywords": joined(md, "subject"),
            "Description": " | ".join(md.get("description", [])),
            "DOI": doi_url,
            "Year Created": joined(md, "date"),
            "Program of Study": extra["Program of Study"],
            "Department": extra["Department"],
            "Advisor": extra["Advisor"],
            "College or School": extra["College or School"],
            "Language": joined(md, "language"),
            "Dissertation or Thesis Type": joined(md, "type")
        }
        print(row)
        writer.writerow(row)

        count += 1
        if count >= LIMIT:
            break

print(f"Exported {count} records to {OUTPUT_CSV}")
