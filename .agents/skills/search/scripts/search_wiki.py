import os
import argparse
import re
import subprocess
from pathlib import Path

def fallback_python_search(target_dir, workspace_root, query):
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    results = []
    
    for root, _, files in os.walk(target_dir):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            file_path = Path(root) / file
            rel_path = file_path.relative_to(workspace_root)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for i, line in enumerate(f, 1):
                        if pattern.search(line):
                            snippet = line.strip()
                            if len(snippet) > 80:
                                snippet = snippet[:80] + "..."
                            results.append(f"{rel_path}:{i}: {snippet}")
            except Exception as e:
                print(f"Error reading {rel_path}: {e}")
                
    return results

def search_wiki(query: str, search_dir: str = None, root_dir: Path = None):
    workspace_root = root_dir or Path(__file__).parent.parent.parent.parent.parent
    wiki_dir = workspace_root / "wiki"
    
    if search_dir:
        target_dir = wiki_dir / search_dir
    else:
        target_dir = wiki_dir
        
    if not target_dir.exists():
        print(f"Directory {target_dir} does not exist.")
        return

    results = []
    
    # Try git grep first for blazing fast performance
    try:
        # --no-index allows it to search untracked files and outside git repos
        proc = subprocess.run(
            ['git', 'grep', '-i', '-n', '--no-index', query], 
            cwd=target_dir, 
            capture_output=True, 
            text=True
        )
        if proc.returncode == 0:
            lines = proc.stdout.splitlines()
            for line in lines:
                parts = line.split(':', 2)
                if len(parts) >= 3:
                    file_name = parts[0]
                    line_num = parts[1]
                    snippet = parts[2].strip()
                    if len(snippet) > 80:
                        snippet = snippet[:80] + "..."
                    
                    # Make relative to workspace
                    rel_path = (target_dir / file_name).relative_to(workspace_root).as_posix()
                    results.append(f"{rel_path}:{line_num}: {snippet}")
        elif proc.returncode == 1:
            # git grep returns 1 if no matches found
            pass
        else:
            # git not installed or some other error, fallback
            results = fallback_python_search(target_dir, workspace_root, query)
    except FileNotFoundError:
        # git is not installed, fallback
        results = fallback_python_search(target_dir, workspace_root, query)

    if not results:
        print(f"No results found for '{query}'")
        return

    print(f"Found {len(results)} matching lines:")
    for res in results[:20]: # Limit to 20 to avoid context bloat
        print(res)
        
    if len(results) > 20:
        print(f"...and {len(results) - 20} more results. Refine your query for more specific results.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search the cervantIA wiki")
    parser.add_argument("--query", type=str, required=True, help="The term to search for")
    parser.add_argument("--dir", type=str, help="Optional specific directory to search (e.g. characters)")
    args = parser.parse_args()
    
    search_wiki(args.query, args.dir)
