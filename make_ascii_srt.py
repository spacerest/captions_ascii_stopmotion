import srt
import datetime

times_list = [srt.ZERO_TIMEDELTA]
srt_list = []
NUM_FRAMES = 100
LEN_VID_MINUTES = 59
LEN_VID_MICROSECONDS = LEN_VID_MINUTES * 1000000
INTERVAL_LEN = datetime.timedelta(microseconds=(LEN_VID_MICROSECONDS / NUM_FRAMES))
OUTPUT_NAME = "test4.srt"
ASCII_SPLIT_CHAR = "?"
ASCII_CONTENT_FILE = "ascii_content_2.txt"
ASCII_TIMING_MODES = ["repeat", "stretch"]
mode_choice = 0

#get list of timedelta intervals
for frame_count in range(NUM_FRAMES - 1):
	microseconds_timedelta = times_list[-1] + INTERVAL_LEN
	times_list.append(
		microseconds_timedelta
		)

#get ASCII content
ascii_content_str = open(ASCII_CONTENT_FILE, "r").read().split(ASCII_SPLIT_CHAR)
print(ascii_content_str[0])

#put ascii content in boxes that match each other
ascii_content_box = open(ASCII_CONTAINER_FILE, "r").read().strip()

#[for ascii_content in ascii_content_str:

#could help with spacing 
#https://stackoverflow.com/questions/9549084/using-pythons-format-specification-mini-language-to-align-floats
ascii_content_split = ascii_content.split("\n")
#todo


#make sure ASCII list matches NUM_FRAMES length
if mode_choice == 0:
	print() 
#todo

#make subtitles
for i, time_start in enumerate(times_list):

	time_end = time_start + INTERVAL_LEN
	try:

		subtitle = srt.Subtitle(
			index=i,
			start=time_start,
			end=time_end,
			content="{\pos(250,270)}" + ascii_content_str[i]
			)
	except IndexError as e:
		print(e)

	
	srt_list.append(subtitle)

new_file = open(OUTPUT_NAME, "w")
new_file.write(srt.compose(srt_list))
