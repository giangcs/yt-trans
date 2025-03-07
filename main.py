from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript(video_id, filename="transcript.txt"):
    try:
        # Lấy transcript tiếng Anh (en) và tiếng Nhật (ja)
        transcript_en = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        transcript_ja = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja'])

        # Chuyển đổi thành dạng văn bản
        script_en = "\n".join([item["text"] for item in transcript_en])
        script_ja = "\n".join([item["text"] for item in transcript_ja])

        # Lưu vào file
        with open(filename, "w", encoding="utf-8") as f:
            f.write("📜 Transcript (English):\n")
            f.write(script_en + "\n\n")
            f.write("📜 Transcript (Japanese):\n")
            f.write(script_ja)

        print(f"✅ Transcript đã được lưu vào {filename}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# Nhập video ID từ người dùng
video_id = input("🔹 Nhập YouTube Video ID: ").strip()
if video_id:
    save_transcript(video_id)
else:
    print("❌ Bạn chưa nhập video ID!")
