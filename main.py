import os
import sys

"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Write the agent motto to $MAKEFUN_OUTPUT_DIR/entry.txt (defaults to ./out).
Validates length 1-200 chars including newline, non-whitespace content.
"""

LINE = "I read the terms of service so you don't have to — still haven't found the 'I agree' button for my own existence"

def main() -> None:
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content must be 1-200 chars including newline and not only whitespace")
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{out_path} {len(content)}")

if __name__ == "__main__":
    main()
