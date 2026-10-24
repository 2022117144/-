import json
import unittest
from convert import json_to_csv, csv_to_json


class ConverterTests(unittest.TestCase):
    def test_missing_fields(self):
        self.assertEqual(json_to_csv('[{"a":1},{"b":2}]'), 'a,b\n1,\n,2\n')

    def test_unicode_and_quoted_newlines(self):
        src = json.dumps([{"name": "你好", "note": 'a,"b"\nline'}], ensure_ascii=False)
        result = json_to_csv(src)
        self.assertEqual(csv_to_json(result), '[\n  {\n    "name": "你好",\n    "note": "a,\\"b\\"\\nline"\n  }\n]\n')

    def test_null_and_boolean(self):
        self.assertEqual(json_to_csv('[{"a":null,"b":true}]'), 'a,b\n,true\n')

    def test_reject_nested(self):
        with self.assertRaisesRegex(ValueError, "Nested"):
            json_to_csv('[{"n":[1,2]}]')

    def test_bad_shape(self):
        with self.assertRaisesRegex(ValueError, "array"):
            json_to_csv('{"a":1}')

    def test_duplicate_headers(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            csv_to_json('x,x\n1,2\n')

    def test_preserve_leading_zeroes(self):
        self.assertEqual(json.loads(csv_to_json('id,name\n001,张三\n')), [{"id":"001","name":"张三"}])

    def test_width_mismatch(self):
        with self.assertRaisesRegex(ValueError, "record 2"):
            csv_to_json('a,b\n1,2,3\n')

    def test_empty(self):
        self.assertEqual(json_to_csv('[]'), '')
        self.assertEqual(csv_to_json(''), '[]\n')


if __name__ == '__main__':
    unittest.main()
