import requests
import xml.etree.ElementTree as ET

url = "https://api.figshare.com/v2/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:figshare.com:article/31069795"

response = requests.get(url, timeout=30)
response.raise_for_status()

xml_text = response.text
root = ET.fromstring(xml_text)

ns = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/",
    "dc": "http://purl.org/dc/elements/1.1/"
}

# Pull all dc:type values
types = [el.text for el in root.findall(".//dc:type", ns) if el.text]

print("Types:", types)

# Simple thesis check
is_thesis = any("thesis" in t.lower() for t in types)

if is_thesis:
    print("This record is a Thesis.")
else:
    print("This record is not marked as a Thesis.")
