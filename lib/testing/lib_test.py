#!/usr/bin/env python3

import pytest
import runpy


class TestNameError:
    def test_name_error(self):
        with pytest.raises(NameError):
            runpy.run_path("lib/a_name_error.py")
