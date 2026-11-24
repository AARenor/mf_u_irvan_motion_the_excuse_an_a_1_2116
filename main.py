"""Write one short line for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

The excuse an AI agent gives its human after losing a bounty.
Standard library only, no network. Writes entry.txt (no trailing newline)
into MAKEFUN_OUTPUT_DIR when set, else /output, and reports the character
count on stderr.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> int:
    # The entry is a single short line: keep it inside the hard limits.
    assert 1 <= len(TEXT) <= 280

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    # Write the exact bytes, with no trailing newline.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
