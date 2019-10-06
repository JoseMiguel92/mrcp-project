# -*- coding: utf-8 -*-

# Created by José Miguel García Benayas

import os
import shutil
import unittest

from graph_utils import GraphUtils


class TableTests(unittest.TestCase):
    CSV_OUTPUT_DIR = "test_files/output"
    CSV_OUTPUT_FILE = "table_test.csv"

    def test_create_table(self):
        if not os.path.isdir(TableTests.CSV_OUTPUT_DIR):
            os.mkdir(TableTests.CSV_OUTPUT_DIR)

        data = dict()
        data.update({'random-1': [100, 45.78, 32, 42, 11]})
        data.update({'random-2': [150, 64.46, 231, 2, 4]})
        try:
            if os.altsep is None:
                file_sep = os.sep
            path = TableTests.CSV_OUTPUT_DIR + file_sep + TableTests.CSV_OUTPUT_FILE
            GraphUtils.create_mrcp_csv_table(path, data)
            self.assertTrue(os.path.isfile(path))
        except IOError:
            self.fail("Test failed.")

        finally:
            if os.path.isdir(TableTests.CSV_OUTPUT_DIR):
                shutil.rmtree(TableTests.CSV_OUTPUT_DIR)


if __name__ == '__main__':
    unittest.main()
