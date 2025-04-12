import unittest
from log_parser import LogParser

class TestLogParser(unittest.TestCase):
    def setUp(self):
        self.parser = LogParser('sample_log.txt')
        self.entries = [
            {'timestamp': '2025-04-11 14:23:10', 'level': 'INFO', 'message': 'System started successfully.'},
            {'timestamp': '2025-04-11 14:24:45', 'level': 'WARNING', 'message': 'High memory usage detected.'},
            {'timestamp': '2025-04-11 14:25:03', 'level': 'ERROR', 'message': 'Failed to connect to database.'}
        ]

    def test_filter_by_level(self):
        filtered = self.parser.filter_by_level(self.entries, 'error')
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]['level'], 'ERROR')

    def test_count_by_level(self):
        count = self.parser.count_by_level(self.entries)
        self.assertEqual(count['INFO'], 1)
        self.assertEqual(count['WARNING'], 1)
        self.assertEqual(count['ERROR'], 1)

if __name__ == '__main__':
    unittest.main()
