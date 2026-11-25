"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph — famous last words, at most
150 characters — to the entry file.

Output path resolution, in order:
  1. $ENTRY_OUTPUT
  2. $OUTPUT_DIR/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
  3. /output/entry.txt
  4. entry.txt next to this script

Standard library only. No network, no file reads outside this script.
"""

import os

EPITAPH = "Tell my boss I died doing what I loved: absolutely nothing, on company time."


def resolve_output_path():
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    output_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return os.path.join(output_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    line = EPITAPH
    if not 1 <= len(line) <= 150:
        raise ValueError("epitaph must be 1-150 characters, got %d" % len(line))
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
