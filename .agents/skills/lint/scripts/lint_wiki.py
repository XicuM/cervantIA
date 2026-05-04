import os
import re
from pathlib import Path

def get_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def lint_yaml(filepath, content, entity_type):
    errors = []
    fm = get_frontmatter(content)
    if not fm:
        return [f"{filepath}: Missing YAML frontmatter"]
        
    required_char = ['name', 'aliases', 'age', 'role', 'status', 'first_appearance']
    required_loc = ['region', 'control_faction']
    
    if entity_type == 'characters':
        for key in required_char:
            if not re.search(fr'^{key}:', fm, re.MULTILINE):
                errors.append(f"{filepath}: Missing '{key}' in YAML")
    elif entity_type == 'locations':
        for key in required_loc:
            if not re.search(fr'^{key}:', fm, re.MULTILINE):
                errors.append(f"{filepath}: Missing '{key}' in YAML")
                
    return errors

def main(root_dir=None):
    workspace_root = root_dir or Path(__file__).parent.parent.parent.parent.parent
    wiki_dir = workspace_root / "wiki"
    
    if not wiki_dir.exists():
        print(f"Error: {wiki_dir} not found.")
        return

    all_files = []
    linked_files = set()
    errors = []
    
    # 1. Collect all files
    for root, _, files in os.walk(wiki_dir):
        for f in files:
            if f.endswith('.md'):
                all_files.append(Path(root) / f)
                
    # 2. Parse files for links and YAML
    for file_path in all_files:
        rel_path = file_path.relative_to(wiki_dir).as_posix()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            errors.append(f"Could not read {rel_path}: {e}")
            continue
            
        # YAML Validation
        if 'characters/' in rel_path:
            errors.extend(lint_yaml(rel_path, content, 'characters'))
        elif 'locations/' in rel_path:
            errors.extend(lint_yaml(rel_path, content, 'locations'))

        # Link Extraction
        # Standard links: [text](path)
        std_links = re.findall(r'\[.*?\]\((.*?\.md)\)', content)
        for link in std_links:
            target_path = (file_path.parent / link).resolve()
            try:
                rel_target = target_path.relative_to(wiki_dir).as_posix()
                linked_files.add(rel_target)
                if not target_path.exists():
                    errors.append(f"{rel_path}: Broken link to '{link}'")
            except ValueError:
                errors.append(f"{rel_path}: Link points outside wiki '{link}'")
                
        # Wikilinks: [[name]]
        wikilinks = re.findall(r'\[\[(.*?)\]\]', content)
        for link in wikilinks:
            # Normalize wikilink to filename
            clean_link = link.split('|')[0].strip() # Handle aliases like [[name|alias]]
            if not clean_link.endswith('.md'):
                clean_link += '.md'
            
            # Simple wikilink resolution: check if any file in all_files ends with this name
            found = False
            for potential in all_files:
                if potential.name == clean_link:
                    found = True
                    linked_files.add(potential.relative_to(wiki_dir).as_posix())
                    break
            if not found:
                errors.append(f"{rel_path}: Broken wikilink to '{link}'")
                
    # 3. Orphan Check
    # We consider files in characters/, locations/, worldbuilding/ orphans if they aren't linked.
    # index.md is expected to link to everything or at least categories.
    for file_path in all_files:
        rel_path = file_path.relative_to(wiki_dir).as_posix()
        if rel_path in ['index.md', 'style_guide.md', 'log.md', 'logs/']: 
            continue
        if rel_path.startswith('logs/'):
            continue
            
        if rel_path not in linked_files:
            # It's an orphan
            errors.append(f"Orphan file: {rel_path} is not linked anywhere.")
            
    # Print Report
    print("=== Wiki Lint Report ===")
    if not errors:
        print("[OK] No errors found! All YAML schemas are valid, no dead links, no orphans.")
    else:
        print(f"[WARN] Found {len(errors)} issues:\n")
        for err in sorted(errors):
            print(f"- {err}")

if __name__ == "__main__":
    main()
