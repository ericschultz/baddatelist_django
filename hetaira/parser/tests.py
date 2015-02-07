from django.test import TestCase
from hetaira.parser import TokenizerError, MessageParser, ParserError

class TestParsing(TestCase):

    def test_phone_numbers_request(self):
        parser = MessageParser()
        possible_numbers = ["9205555555", " 9205555555", "9205555555 ", " (92055555)5-5 "]
        results = map(lambda x: parser.parse(x), possible_numbers)
        for r in results:
            self.assertEqual(type(r).__name__, "Request")
            self.assertEqual(r.req_id, "9205555555")


    def test_email_address_request(self):
        parser = MessageParser()
        possible_emails = ["something@not.test", " something@not.test "]
        results = map(lambda x: parser.parse(x), possible_emails)
        for r in results:
            self.assertEqual(type(r).__name__, "Request")
            self.assertEqual(r.req_id, "something@not.test")


    def test_license_request(self):
        parser = MessageParser()
        possible_license = ["WI*152510fC", " WI*152510fC "]
        results = map(lambda x: parser.parse(x), possible_license)
        for r in results:
            self.assertEqual(type(r).__name__, "Request")
            self.assertEqual(r.req_id, "WI*152510fC")

    def test_phone_numbers_response(self):
        parser = MessageParser()
        possible_reports = ["9205555555 NC DR PO ST PH",
            " 9205555555 NC DR PO ST PH", "9205555555  NC DR PO ST PH",
            " (92055555)5-5  N-C D(R PO S)T PH"]

        results = map(lambda x: parser.parse(x), possible_reports)
        for r in results:
            self.assertEqual(type(r).__name__, "Report")
            self.assertEqual(r.req_id, "9205555555")
            self.assertItemsEqual(r.conditions, ["NC", "DR", "PO", "ST", "PH"])

    def test_tokenizer_exception(self):
        parser = MessageParser()
        possible_ids = ["5444444444444444", "WI", "So at ba", "AA"]

        for req_id in possible_ids:
            with self.assertRaises(TokenizerError) as cm:
                parser.parse(req_id)
            exception = cm.exception
            self.assertEqual(exception.code, TokenizerError.INVALID_TOKEN)


    def test_parsing_exception_expected_ID(self):
        parser = MessageParser()
        possible_ids = ["NP"]

        for req_id in possible_ids:
            with self.assertRaises(ParserError) as cm:
                parser.parse(req_id)
            exception = cm.exception
            self.assertEqual(exception.code, ParserError.UNEXPECTED_CONDITION)
