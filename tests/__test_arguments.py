import os
import sys

import pytest
import argparse
from server import check_file
from server import app
from server import main

scenarios = [
    ('scenario1', {"opt1":"-f", "para1":"test.txt",
                   "opt2":"-p", "para2":"12346"}),
    ('scenario2', dict(opt="-h")),
    ('scenario3', dict(opt='ggg'))
]

def pytest_generate_tests(metafunc):
    idlist = []
    argvalues = []
    for scenario in metafunc.cls.scenarios:
        idlist.append(scenario[0])
        items = scenario[1].items()
        argnames = [x[0] for x in items]
        argvalues.append([x[1] for x in items])
    metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")

def test_arguments():

    file, port = main()
    assert file == "test.txt"
    assert port == 23456

def test_bad_argument(capsys):
    sys.stdin.write("-g ghghg -k tyytter")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        file, port = main()
        captured = capsys.readouterr()
        assert "server.py [-f <filename>] [-p <port>]" in captured.out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 42

def test_help_argument(capsys):
    sys.stdin.write("-h -f test.txt")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        file, port = main()
        captured = capsys.readouterr()
        assert "server.py [-f <filename>] [-p <port>]" in captured.out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 42
