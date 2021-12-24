"""YAML tool, a clone of the json.tool Python module for YAML.

This tool provides a simple command line interface to validate and pretty-print
YAML documents while trying to preserve as much as possible from the original
documents (like comments and anchors).
"""


import argparse
import pathlib
import sys
import textwrap
import ruamel.yaml  # pylint: disable=import-error


def main():
    """Main entrypoint."""
    epilog = textwrap.dedent(
        """
        When enabling --in-place, all files are processed as input files.
        When --in-place is not enabled and there are more then 2 files
        passed, the last files is considered as the output file. If you
        wish to pretty-print multiple files and output to standard out,
        specify the last file as "-" .
        Please note that specifying multiple input files will concatenate
        them, resulting in a single file that has multiple documents."""
    )
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=pathlib.Path,
        help="a YAML file to be validated or pretty-printed",
    )
    parser.add_argument(
        "-i",
        "--in-place",
        help="Perform the pretty-print in place, overwriting the existing files.",  # noqa: E501
        action="store_true",
    )
    options = parser.parse_args()
    try:
        yaml = ruamel.yaml.YAML(typ="rt")
        yaml.explicit_start = True
        yaml.indent(mapping=2, sequence=4, offset=2)
        yaml.preserve_quotes = True
        if options.in_place:
            if len(options.files) == 0:
                raise Exception("You must provide a list of files to process.")
            for file in options.files:
                with open(file, "r", encoding="utf-8") as infile:
                    docs = list(yaml.load_all(infile))
                with open(file, "w", encoding="utf-8") as outfile:
                    yaml.dump_all(docs, outfile)
        else:
            if len(options.files) < 2:
                outfile = sys.stdout
            elif options.files[-1] == "-":
                outfile = sys.stdout
                options.files.pop(-1)
            else:
                outfile = open(  # pylint: disable=consider-using-with
                    options.files[-1], "w", encoding="utf-8"
                )
                options.files.pop(-1)
            if options.files:
                for file in options.files:
                    with open(file, "r", encoding="utf-8") as infile:
                        yaml.dump_all(yaml.load_all(infile), outfile)
            else:
                yaml.dump_all(yaml.load_all(sys.stdin), outfile)
    except Exception as ex:
        raise SystemExit(ex)  # pylint: disable=raise-missing-from


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError as exc:
        sys.exit(exc.errno)
