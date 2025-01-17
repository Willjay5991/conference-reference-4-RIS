import json
 
def json_to_ris(json_data, output_file):
    year = "2024"
    journal = "iclr"
    with open(output_file, 'w', encoding='utf-8') as f:
        for item in json_data:
            # Write RIS header
            f.write("TY  - JOUR\n")
 
            # Title
            f.write(f"TI  - {item['title']}\n")
 
            # Authors
            authors = ', '.join(item['author'])
            f.write(f"AU  - {authors}\n")
 
            # Year
            f.write(f"PY  - {year}\n")
 
            # Journal
            f.write(f"JO  - {journal}\n")

 
            # End of record
            f.write("ER  - \n\n")
    print(f"Converted {len(json_data)} records to RIS format and saved to {output_file}")
 
# read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    

# Example JSON data
json_data = [
    {
        "title": "An Example Paper",
        "authors": ["John Doe", "Jane Smith"],
        "year": 2023,
        "journal": "Journal of Examples",
        "volume": "1",
        "issue": "1",
        "pages": "1-10",
        "doi": "10.1234/example"
    }
]

path = "./iclr2024.json"
json_data = read_json_file(path)
# Convert and save to RIS file
json_to_ris(json_data, 'output.ris')