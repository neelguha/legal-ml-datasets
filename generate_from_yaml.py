#!/usr/bin/env python3
"""
Generate README.md from datasets.yaml
- Properly alphabetizes entries
- Validates data
- Supports optional metadata fields
"""

import yaml
import os
import sys
from urllib.parse import urlparse

DESCRIPTION = """This is a collection of pointers to datasets/tasks/benchmarks pertaining to the intersection of machine learning and law.

This page is continually being updated. If there's a dataset/resource you think should be included here, please make a pull request adding it, or contact me at nguha@stanford.edu and I'll add it!

A spreadsheet corresponding to the papers listed here can be found [here](https://docs.google.com/spreadsheets/d/11o7R3TRtREbDcxcbCMUERu5WRZsgLZtTaRFUhr4jLtk/edit?usp=sharing).

Neel Guha"""

TITLE = "# Datasets for Machine Learning in Law"

def validate_entry(entry, index):
    """Validate a dataset entry."""
    errors = []
    if not entry.get('title', '').strip():
        errors.append(f"Entry {index + 1}: Missing title")
    if not entry.get('url', '').strip():
        errors.append(f"Entry {index + 1}: Missing URL")
    else:
        url = entry['url'].strip()
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            errors.append(f"Entry {index + 1}: Invalid URL: {url}")
    if not entry.get('abstract', '').strip():
        errors.append(f"Entry {index + 1}: Missing abstract")
    return errors

def check_duplicates(datasets):
    """Check for duplicate titles or URLs."""
    titles = {}
    urls = {}
    duplicates = []
    
    for idx, dataset in enumerate(datasets):
        title = dataset.get('title', '').strip().lower()
        url = dataset.get('url', '').strip().lower()
        
        if title in titles:
            duplicates.append(f"Duplicate title: '{dataset.get('title')}' (entries {titles[title] + 1} and {idx + 1})")
        else:
            titles[title] = idx
            
        if url in urls:
            duplicates.append(f"Duplicate URL: '{dataset.get('url')}' (entries {urls[url] + 1} and {idx + 1})")
        else:
            urls[url] = idx
    
    return duplicates

def generate_readme(input_file, output_file, validate=True):
    """Generate README.md from YAML file."""
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return False
    
    # Load YAML
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return False
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    # Extract datasets
    if 'datasets' not in data:
        print("Error: 'datasets' key not found in YAML file.")
        return False
    
    datasets = data['datasets']
    
    if not datasets:
        print("Error: No datasets found in YAML file.")
        return False
    
    # Validate entries
    if validate:
        for idx, entry in enumerate(datasets):
            errors = validate_entry(entry, idx)
            if errors:
                for error in errors:
                    print(f"Warning: {error}")
    
    # Check for duplicates
    if validate:
        duplicates = check_duplicates(datasets)
        if duplicates:
            print("Warnings:")
            for dup in duplicates:
                print(f"  {dup}")
    
    # Sort alphabetically by title (case-insensitive)
    datasets.sort(key=lambda x: x.get('title', '').lower())
    
    # Generate the README content
    readme_content = TITLE + "\n\n" + DESCRIPTION + "\n\n ---\n\n"
    
    for dataset in datasets:
        title = dataset.get('title', '').strip()
        url = dataset.get('url', '').strip()
        abstract = dataset.get('abstract', '').strip()
        
        readme_content += f"### [{title}]({url})\n\n"
        readme_content += f">{abstract}\n\n"
    
    # Write the README file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Successfully generated README.md with {len(datasets)} entries.")
    return True

if __name__ == "__main__":
    input_file = "datasets.yaml"
    output_file = "README.md"
    
    # Allow override via command line
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    validate = "--no-validate" not in sys.argv
    generate_readme(input_file, output_file, validate=validate)

