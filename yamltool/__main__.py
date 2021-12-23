"""YAML tool, a clone of the json.tool Python module for YAML.

This tool provides a simple command line interface to validate and pretty-print
YAML documents while trying to preserve as much as possible from the original
documents (like comments and anchors).
"""


import argparse
import pathlib
import sys
import ruamel.yaml  # pylint: disable=import-error


def main():
    """Main entrypoint."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType(encoding="utf-8"),
        help="a YAML file to be validated or pretty-printed",
        default=sys.stdin,
    )
    parser.add_argument(
        "outfile",
        nargs="?",
        type=pathlib.Path,
        help="write the output of infile to outfile",
        default=None,
    )
    options = parser.parse_args()
    with options.infile as infile:
        try:
            yaml = ruamel.yaml.YAML(typ="rt")
            yaml.explicit_start = True
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.preserve_quotes = True
            if options.outfile is None:
                out = sys.stdout
            else:
                out = options.outfile.open("w", encoding="utf-8")
            yaml.dump_all(yaml.load_all(infile), out)
        except Exception as ex:
            raise SystemExit(ex)  # pylint: disable=raise-missing-from


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError as exc:
        sys.exit(exc.errno)
