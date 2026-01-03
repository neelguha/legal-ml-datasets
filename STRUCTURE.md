# Project Structure and Workflow

## Overview

This repository maintains a curated list of legal ML datasets. The recommended workflow uses **YAML as the single source of truth** and generates the README automatically.

## File Structure

- `datasets.yaml` - **Source of truth** - All dataset entries in YAML format (human-readable!)
- `README.md` - Generated from YAML (do not edit manually)
- `generate_from_yaml.py` - Script to generate README from YAML (with validation and auto-sorting)
- `STRUCTURE.md` - This documentation file

## Recommended Workflow

### Adding a New Dataset

1. **Add to YAML file** (`datasets.yaml`):
   ```yaml
   datasets:
     - title: "My New Dataset"
       url: "https://example.com"
       abstract: "This is a great dataset for..."
       # Optional metadata:
       domain: "Case Law"
       language: "English"
       year: 2024
       tags: ["benchmark", "multiple-choice"]
   ```

2. **Generate README**:
   ```bash
   python3 generate_from_yaml.py
   ```

3. **Commit both files**:
   ```bash
   git add datasets.yaml README.md
   git commit -m "Add new dataset: My New Dataset"
   ```

### YAML Format Benefits

- **Human-readable**: Much easier to edit than TSV
- **Supports lists**: Tags, languages, etc. can be arrays
- **Comments**: Add notes with `#`
- **Structured data**: Nested objects if needed
- **Optional fields**: Only include what you need

Example with optional metadata:
```yaml
- title: "CaseHOLD"
  url: "https://arxiv.org/abs/2104.08671"
  abstract: "A dataset for case holdings..."
  domain: "Case Law"
  language: "English"
  year: 2021
  tags: ["benchmark", "multiple-choice", "case-law"]
```

## Scripts

### `generate_from_yaml.py`

Generates README from YAML with:
- ✅ Proper alphabetical sorting
- ✅ Data validation (checks for missing fields, invalid URLs)
- ✅ Duplicate detection

```bash
python3 generate_from_yaml.py
python3 generate_from_yaml.py datasets.yaml README.md
python3 generate_from_yaml.py --no-validate  # Skip validation
```

### `tsv_to_yaml.py` (Migration)

Convert old TSV format to YAML:

```bash
python3 tsv_to_yaml.py papers.tsv datasets.yaml
```

## Best Practices

1. **Always edit YAML, not README** - README is generated automatically
2. **Run validation** - Use `generate_from_yaml.py` to catch errors early
3. **Keep entries alphabetized** - The generate script does this automatically
4. **Use consistent formatting** - Follow existing abstract style
5. **Add metadata** - Use domain, language, year, tags fields for better organization
6. **Use YAML lists** - For tags and languages: `tags: ["tag1", "tag2"]`

## Migration from TSV to YAML

**Note:** Migration to YAML is complete. The repository now uses YAML as the single source of truth.

If you need to convert TSV files in the future:

```bash
# Convert TSV to YAML
python3 tsv_to_yaml.py input.tsv datasets.yaml

# Regenerate README from YAML
python3 generate_from_yaml.py
```

## Future Enhancements

Consider adding:
- Automatic URL validation/checking
- Integration with spreadsheet (Google Sheets API)
- CI/CD to auto-generate README on PR
- YAML schema validation (using JSON Schema or similar)
- Automatic categorization/tagging
- Link checking to detect broken URLs
- Pre-commit hook to auto-generate README before commits

