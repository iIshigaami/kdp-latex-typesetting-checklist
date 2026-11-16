#!/usr/bin/env python3
"""Compute a KDP wraparound-cover spine width from page count and paper type.

Uses the calipers published in Amazon KDP's help pages:
  cream (black & white) : 0.0025   in per page
  white (black & white) : 0.002252 in per page
  color                 : 0.002347 in per page

This is pure arithmetic. It cannot know your final compiled page count, so
re-run it after the last build. Verify against current KDP documentation.

Reference: https://kdp.amazon.com/en_US/help/topic/G201953020
"""

import argparse

CALIPERS_IN = {
    "cream": 0.0025,
    "white": 0.002252,
    "color": 0.002347,
}

MM_PER_INCH = 25.4


def spine_inches(pages: int, paper: str) -> float:
    """Return spine width in inches for the given page count and paper."""
    if pages < 24:
        raise ValueError("KDP paperbacks require at least 24 pages")
    return pages * CALIPERS_IN[paper]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pages", type=int, help="final compiled page count")
    parser.add_argument("--paper", choices=CALIPERS_IN, default="cream")
    args = parser.parse_args()

    width = spine_inches(args.pages, args.paper)
    print(
        f"{args.pages} pages on {args.paper} paper: "
        f"spine {width:.4f} in / {width * MM_PER_INCH:.3f} mm"
    )


if __name__ == "__main__":
    main()
