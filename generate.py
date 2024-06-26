"""
This python script was generated by Claude!
"""

import csv
from collections import defaultdict
import os

DESCRIPTION = """This is a collection of pointers to datasets/tasks/benchmarks pertaining to the intersection of machine learning and law.

This page is continually being updated. If there's a dataset/resource you think should be included here, please make a pull request adding it, or contact me at nguha@stanford.edu and I'll add it!

A spreadsheet corresponding to the papers listed here can be found [here](https://docs.google.com/spreadsheets/d/11o7R3TRtREbDcxcbCMUERu5WRZsgLZtTaRFUhr4jLtk/edit?usp=sharing).

Neel Guha"""

TITLE="# Datasets for Machine Learning in Law"

def generate_readme(input_file, output_file):
    # Read the TSV file
    papers = defaultdict(list)
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            papers[row['Title']].append(row)

    # Sort the papers alphabetically
    sorted_letters = sorted(papers.keys())

    # Generate the README content
    readme_content = TITLE + "\n\n" + DESCRIPTION + "\n\n ---\n\n"
    
    for letter in sorted_letters:
        for paper in sorted(papers[letter], key=lambda x: x['Title'].lower()):
            readme_content += f"### [{paper['Title']}]({paper['URL']})\n\n"
            #readme_content += f"**URL:** [{paper['URL']}]({paper['URL']})\n\n"
            readme_content += f">{paper['Abstract']}\n\n"
        readme_content += "\n"

    # Write the README file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    input_file = "papers.tsv"  # Replace with your input TSV file name
    output_file = "README.md"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
    else:
        generate_readme(input_file, output_file)
        print(f"README.md has been generated successfully.")