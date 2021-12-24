YAML tool
#########

.. image:: https://git.shore.co.il/nimrod/yamltool/badges/main/pipeline.svg
    :target: https://git.shore.co.il/nimrod/yamltool/-/commits/main
    :alt: pipeline status

YAML tool, a clone of the json.tool Python module for YAML.

This tool provides a simple command line interface to validate and pretty-print
YAML documents while trying to preserve as much as possible from the original
documents (like comments and anchors).

Usage
-----

.. code:: shell

    usage: yt [-h] [-i] [files ...]

    YAML tool, a clone of the json.tool Python module for YAML.

    This tool provides a simple command line interface to validate and pretty-print
    YAML documents while trying to preserve as much as possible from the original
    documents (like comments and anchors).

    positional arguments:
      files           a YAML file to be validated or pretty-printed

    optional arguments:
      -h, --help      show this help message and exit
      -i, --in-place  Perform the pretty-print in place, overwriting the existing files.

    When enabling --in-place, all files are processed as input files.
    When --in-place is not enabled and there are more then 2 files
    passed, the last files is considered as the output file. If you
    wish to pretty-print multiple files and output to standard out,
    specify the last file as "-" .
    Please note that specifying multiple input files will concatenate
    them, resulting in a single file that has multiple documents.

pre-commit hook
---------------

YAML tool can be used as a `pre-commit <https://pre-commit.com/>` hook by
adding the following to your :code:`.pre-commit-config.yaml` file:

.. code:: yaml

    ---
    repos:
      - repo: https://git.shore.co.il/nimrod/yamltool.git
        rev: 0.1.0  # Check for the latest tag or run pre-commit autoupdate.
        hooks:
          - id: yamltool

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author
------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/nimrod/.
