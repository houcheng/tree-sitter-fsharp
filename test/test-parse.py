from tree_sitter import Parser
from tree_sitter_languages import get_language
import os
import glob
from pathlib import Path


def parse_fsharp_file(file_path, is_invalid_ok=False):
    parser = Parser()
    fsharp_language = get_language('fsharp')
    parser.set_language(fsharp_language)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            source_code = f.read()

        tree = parser.parse(bytes(source_code, 'utf-8'))
        root_node = tree.root_node

        if root_node is None:
            if is_invalid_ok:
                print(f"✓ Parse failed but acceptable for {file_path}")
                return True
            print(f"✗ Failed parsing {file_path}")
            return False

        print(f"✓ Successfully parsed {file_path}")
        return True

    except Exception as e:
        if is_invalid_ok:
            print(f"✓ Parse error but acceptable for {file_path}: {str(e)}")
            return True
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False


def expand_glob_patterns(patterns):
    files = set()
    for pattern in patterns:
        pattern = pattern.strip()
        if pattern:
            pattern = str(Path(pattern))
            expanded = glob.glob(pattern, recursive=True)
            files.update(expanded)
    return sorted(list(files))


def main():
    # Track statistics
    stats = {
        'valid_success': 0,
        'valid_failure': 0,
        'invalid_files_processed': 0,
    }

    # Read valid files
    try:
        with open("test/files.txt", 'r') as f:
            valid_patterns = f.read().splitlines()
        valid_files = expand_glob_patterns(valid_patterns)
    except Exception as e:
        print(f"Error reading files.txt: {str(e)}")
        return

    # Read invalid-ok files
    try:
        with open("test/invalid-files.txt", 'r') as f:
            invalid_patterns = f.read().splitlines()
        invalid_files = expand_glob_patterns(invalid_patterns)
    except Exception as e:
        print(f"Error reading invalid-files.txt: {str(e)}")
        return

    print("\nProcessing valid files:")
    print("=" * 50)
    for file_path in valid_files:
        if os.path.exists(file_path):
            if parse_fsharp_file(file_path):
                stats['valid_success'] += 1
            else:
                stats['valid_failure'] += 1
        else:
            print(f"File not found: {file_path}")
            stats['valid_failure'] += 1

    print("\nProcessing files that may fail:")
    print("=" * 50)
    for file_path in invalid_files:
        if os.path.exists(file_path):
            parse_fsharp_file(file_path, is_invalid_ok=True)
            stats['invalid_files_processed'] += 1
        else:
            print(f"File not found: {file_path}")

    # Print summary
    print("\nTest Summary:")
    print("=" * 50)
    print("Valid files:")
    print(f"  Passed: {stats['valid_success']}")
    print(f"  Failed: {stats['valid_failure']}")
    print(f"Files that may fail: {stats['invalid_files_processed']}")

    valid_total = stats['valid_success'] + stats['valid_failure']
    if valid_total > 0:
        success_rate = (stats['valid_success'] / valid_total * 100)
        print(f"\nSuccess rate for valid files: {success_rate:.1f}%")


if __name__ == "__main__":
    main()
