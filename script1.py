
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "UsWSANcm4Q4"
items = YouTubeTranscriptApi.get_transcript(video_id)

for item in items:
    text = item["text"]
    start = item["start"]
    duration = item["duration"]
    end = start + duration

    print(f"\ntext: {text}\nstart: {start:.2f}\nend: {end:.2f}")

