# import os
# import json
# from datetime import datetime

# def get_metadata(file):
#     """Extract metadata for each HTML file."""
    
#     created = datetime.fromtimestamp(os.stat(file).st_birthtime).strftime('%Y-%m-%d')
#     modified = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
#     return {"url": file, "title": os.path.splitext(file)[0].title(), "date_created": created, "date_modified": modified}

# files = [get_metadata(f) for f in os.listdir('.') if f.endswith('.html')]

# with open('files.json', 'w') as f:
#     json.dump(files, f, indent=2)

# print(f"Generated files.json with {len(files)} files.")

import os
import json
from datetime import datetime
from bs4 import BeautifulSoup

def get_metadata(file):
    """Extract metadata (title, date_created, and date_modified) for an HTML file."""
    # Open and parse the HTML file
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # Extract title from <meta> tags or <title>
    # title = (soup.find('meta', {'name': 'title'}) or {}).get('content') or soup.title.string or "Untitled"
    title = (soup.find('meta', {'name': 'title'}) or {}).get('content') or "Untitled"
    
    # Extract file dates (file system based)
    created = datetime.fromtimestamp(os.stat(file).st_birthtime).strftime('%Y-%m-%d')
    modified = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
    
    return {
        "url": file,
        "title": title.strip(),
        "date_created": created,
        "date_modified": modified
    }

def main():
    # Filter for HTML files in the current directory
    files = [get_metadata(f) for f in os.listdir('.') if f.endswith('.html')]
    
    # Write metadata to files.json
    with open('files.json', 'w', encoding='utf-8') as f:
        json.dump(files, f, indent=2)
    
    print(f"Generated files.json with metadata for {len(files)} HTML files.")

if __name__ == "__main__":
    main()
