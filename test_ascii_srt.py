import unittest
from ascii_srt import AsciiSrtFactory
from datetime import datetime
import srt

class TestAsciiSrtFactory(unittest.TestCase):
	def test_empty_srt_count(self):
		factory = AsciiSrtFactory(None)
		factory.ascii_content_str = factory.ascii_split_char
		factory.make_subtitles()
		self.assertEqual(len(factory.srt_list), 1)

	def test_empty_srt_starts_at_zero(self):
		factory = AsciiSrtFactory(None)
		factory.ascii_content_str = factory.ascii_split_char
		factory.make_subtitles()
		self.assertEqual(factory.srt_list[0].start, srt.ZERO_TIMEDELTA)

	def test_empty_srt_ends_at_zero(self):
		factory = AsciiSrtFactory(None, video_minutes=0)
		factory.ascii_content_str = factory.ascii_split_char
		factory.make_subtitles()
		self.assertEqual(factory.srt_list[0].end, srt.ZERO_TIMEDELTA)

	def test_writes_srt_to_file(self):
		factory = AsciiSrtFactory(None, video_minutes=1, output_fn='test_output.srt')
		factory.ascii_content_str = factory.ascii_split_char
		factory.make_subtitles()
		factory.write_srt_to_file()
		result_srt_list = list(srt.parse(open('test_output.srt').read()))
		self.assertEqual(factory.srt_list, result_srt_list)

	def test_gets_ascii_content_from_input_file(self):
		factory = AsciiSrtFactory('test_res/test_ascii_input1.txt', video_minutes=1)
		factory.read_ascii_content()
		factory.make_subtitles()
		factory.write_srt_to_file()

		self.assertEqual(factory.srt_list[0].content, "hello\n")
		self.assertEqual(factory.srt_list[1].content, "world\n")



if __name__ == '__main__':
    unittest.main()