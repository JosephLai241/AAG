import argparse

from aag.utils import Cli

class MakeArgs():
    """
    Making dummy args to test Cli.py functions.
    """

    @staticmethod
    def parser_for_testing_cli():
        parser = argparse.ArgumentParser()
        return parser

    @staticmethod
    def make_generator_args():
        parser = MakeArgs.parser_for_testing_cli()
        parser.add_argument("--list")
        parser.add_argument("--examples")
        parser.add_argument("--make")
        parser.add_argument("--randomize")

class TestParserInitMethod():
    """
    Testing Parser class __init__() method found on line 14 in Cli.py.
    """

    def test_parser_init_method_usage_instance_variable(self):
        usage = "$ AAG.py [-h] [-l] [-e] [-m FONT_NUM TEXT] [-r TEXT]"

        assert Cli.Parser()._usage == usage

    def test_parser_init_method_description_instance_variable(self):
        description = r"""
Ascii Art Generator - Generate art from 425 fonts

Author: Joseph Lai
"""

        assert Cli.Parser()._description == description

    def test_parser_init_method_epilog_instance_variable(self):
        epilog = r"""
EXAMPLES

List all available fonts:

    $ ./AAG.py -l

Generate examples for all fonts:

    $ ./AAG.py -e

Create ASCII art using the "larry3d" font:

    $ ./AAG.py -m 211 something

Wrap your text in quotes if it is more than one word or contains special characters:

    $ ./AAG.py -m 211 "ASCII Art Generator"

    $ ./AAG.py -m 330 "H&M"

Generate ASCII art from a random font:

    $ ./AAG.py -r "A random font"
"""

        assert Cli.Parser()._epilog == epilog

class TestParserAddFlagsMethod():
    """
    Testing Parser class _add_flags() method found on line 48 in Cli.py.
    """

    def test_add_flags_method_list_flag(self):
        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args(["--list"])

        assert args.list == True

    def test_add_flags_method_examples_flag(self):
        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args(["--examples"])

        assert args.examples == True

    def test_add_flags_method_make_flag(self):
        test_make_args = [["330", "TEST"]]

        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args("--make 330 TEST".split())

        assert args.make == test_make_args

    def test_add_flags_method_randomize_flag(self):
        test_make_args = ["TEST"]

        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args("--randomize TEST".split())

        assert args.randomize == test_make_args

class TestCheckArgsCheckMakeMethod():
    """
    Testing CheckArgs class check_make() method found on line 89 in Cli.py.
    """

    def test_check_make_valid_args(self):
        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args("--make 330 TEST".split())

        try:
            Cli.CheckArgs.check_make(args, parser)
            assert True
        except SystemExit:
            assert False

    def test_check_make_valid_args(self):
        parser = MakeArgs.parser_for_testing_cli()
        Cli.Parser()._add_flags(parser)

        args = parser.parse_args("--make asdf TEST".split())

        try:
            Cli.CheckArgs.check_make(args, parser)
            assert False
        except SystemExit:
            assert True
