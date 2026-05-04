import os
from pathlib import Path

def generate_index(root_dir=None):
    workspace_root = root_dir or Path(__file__).parent.parent.parent.parent.parent
    wiki_dir = workspace_root / "wiki"
    index_path = wiki_dir / "index.md"
    
    if not wiki_dir.exists():
        print(f"Error: {wiki_dir} not found.")
        return

    content = [
        "# Wiki Index",
        "",
        "Catalog of all structured knowledge entities. (Auto-generated)",
        ""
    ]
    
    directories = [
        ("Characters", "characters"),
        ("Locations", "locations"),
        ("Plot", "plot"),
        ("Worldbuilding", "worldbuilding")
    ]
    
    for title, dir_name in directories:
        content.append(f"## {title}")
        target_dir = wiki_dir / dir_name
        
        if not target_dir.exists() or not any(target_dir.iterdir()):
            content.append("*(Empty)*\n")
            continue
            
        # Get markdown files
        md_files = sorted([f for f in os.listdir(target_dir) if f.endswith('.md')])
        if not md_files:
            content.append("*(Empty)*\n")
            continue
            
        for f in md_files:
            # Create link text by removing .md and replacing underscores/dashes with spaces
            link_text = f.replace('.md', '').replace('_', ' ').replace('-', ' ').title()
            # If it's timeline, preserve original case or let title do it
            content.append(f"- [{link_text}]({dir_name}/{f})")
            
        content.append("")
        
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))
        print("[OK] Successfully generated wiki/index.md")
    except Exception as e:
        print(f"Error writing index.md: {e}")

if __name__ == "__main__":
    generate_index()
