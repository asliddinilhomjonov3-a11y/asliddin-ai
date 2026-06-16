from moviepy.editor import VideoFileClip, concatenate_videoclips

# Fayl nomlari aynan papkadagi nomlar bilan bir xil bo'lishi kerak
video1 = VideoFileClip("video1.mp4")
video2 = VideoFileClip("video2.mp4")

# Birlashtirish
final_video = concatenate_videoclips([video1, video2])

# Saqlash
final_video.write_videofile("natija.mp4")
print("Video tayyor bo'ldi: natija.mp4")