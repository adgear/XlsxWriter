###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2019, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparsion_test import ExcelComparisonTest
from ...workbook import Workbook


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('textbox30.xlsx')

        self.ignore_elements = {'xl/drawings/drawing1.xml': ['<a:pPr/>']}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with textbox(s)."""

        workbook = Workbook(self.got_filename)

        worksheet = workbook.add_worksheet()

        worksheet.write('A1', 'This is some text')
        worksheet.insert_textbox('E9', 'This is some text', {'textlink': '=$A$1'})

        workbook.close()

        self.assertExcelEqual()
