#%%

import pandas as pd
from dateutil import parser

df = pd.read_excel('papers.ods')
output_lines = []

for _, row in reversed(list(df.iterrows())):
    title = row["title"]
    authors = row["authors"]
    venue = row["conference"]
    date = row["date"].strftime("%B %Y")
    
    
    links = []
    if not pd.isna(row["demo"]):
        links.append(f"[Demo]({row['demo']})")
    if not pd.isna(row["pdf"]):
        links.append(f"[PDF](files/{row['pdf']})")
    if not pd.isna(row["conference_link"]):
        if row["type"] == "Conference Paper" or row["type"] == "Demo Paper":
            links.append(f"[Conference]({row['conference_link']})")
        if row["type"] == "Journal Paper":
            links.append(f"[Journal]({row['conference_link']})")
    if not pd.isna(row["arxiv"]):
        links.append(f"[arXiv]({row['arxiv']})")
    if not pd.isna(row["poster"]):
        links.append(f"[Poster](files/{row['poster']})")
    if not pd.isna(row["video"]):
        links.append(f"[Video Presentation]({row['video']})")
    
    links_str = " · ".join(links)
    
    block = (
        f"**{title}**\\\n"
        f"{authors}.\\\n"
        f"{venue}, {date}.\\\n"
        f"{links_str}"
    )
    
    output_lines.append(block)

# Combine all entries with a blank line between them
markdown_output = "\n\n".join(output_lines)


print(markdown_output)
