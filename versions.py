import subprocess
import re
import json
import sys

def get_git_tags():
    """Retrieve all tags from the Git repository."""
    try:
        tags = subprocess.check_output(["git", "tag"], text=True)
        return tags.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching git tags: {e}")
        sys.exit(1)

def extract_build_numbers(tags, version):
    """Extract build numbers for a specific version from the list of tags."""
    version_pattern = re.compile(rf"^{re.escape(version)}\\.(\\d+)$")
    build_numbers = []

    for tag in tags:
        match = version_pattern.match(tag)
        if match:
            build_numbers.append(int(match.group(1)))

    return build_numbers

def get_latest_and_next_build(version):
    """Return the latest and next build numbers for the specified version."""
    tags = get_git_tags()
    build_numbers = extract_build_numbers(tags, version)

    if build_numbers:
        latest_build = max(build_numbers)
        next_build = latest_build + 1
    else:
        latest_build = None
        next_build = 0

    return {
        "latest": latest_build,
        "next": next_build
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <version>")
        sys.exit(1)

    version = sys.argv[1]
    result = get_latest_and_next_build(version)
    print(json.dumps(result))

if __name__ == "__main__":
    main()
