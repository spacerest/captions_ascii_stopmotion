import srt
import datetime
import pdb
import logging

logging.basicConfig(filename='errors.log',
	level=logging.DEBUG,
	filemode='w', 
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class AsciiSrtFactory():

	def __init__(self, ascii_source_fn, output_fn='output.srt', num_frames=60, video_minutes=1):
		self.times_list = [srt.ZERO_TIMEDELTA]
		self.srt_list = []
		self.num_frames = num_frames
		self.len_vid_minutes = video_minutes
		self.len_vid_microseconds = self.len_vid_minutes * 10000000 * 60.0
		self.interval_len = datetime.timedelta(microseconds=(self.len_vid_microseconds / self.num_frames))
		self.output_name = output_fn
		self.ascii_split_char = "?"
		self.ascii_container_file = "ascii_content_2.txt"
		self.ascii_source_fn = ascii_source_fn
		self.ascii_timing_modes = ["repeat", "stretch"]
		self.mode_choice = 0

	def get_timedelta_intervals(self):
		#make sure ASCII list matches num_frames length
		if mode_choice == 0:
			#todo
			print() 
		#get list of timedelta intervals
		for frame_count in range(self.num_frames - 1):
			microseconds_timedelta = times_list[-1] + self.interval_len
			self.times_list.append(
				microseconds_timedelta
				)

	def read_ascii_content(self):
		#get ASCII content
		self.ascii_content_str = open(self.ascii_source_fn, "r").read().split(self.ascii_split_char)
		loggin.debug(self.ascii_content_str)

	def frame_ascii_content(self):
		#put ascii content in boxes that match each other
		ascii_content_box = open(ascii_container_file, "r").read().strip()
		#could help with spacing 
		#https://stackoverflow.com/questions/9549084/using-pythons-format-specification-mini-language-to-align-floats
		ascii_content_split = ascii_content_box.split("\n")
		#todo

	def make_subtitles(self):
		#make subtitles
		for i, time_start in enumerate(self.times_list):
			time_end = time_start + self.interval_len
			try:
				subtitle = srt.Subtitle(
					index=i+1,
					start=time_start,
					end=time_end,
					content=self.ascii_content_str[i]
					)
				self.srt_list.append(subtitle)
			except IndexError as e:
				logging.error(e)

	def write_srt_to_file(self):
		new_file = open(self.output_name, "w")
		logging.debug(f"{self.output_name}")
		logging.debug(f"{self.srt_list=}")
		new_file.write(srt.compose(self.srt_list))
