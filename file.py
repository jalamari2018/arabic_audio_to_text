import whisper

model = whisper.load_model("base")
result = model.transcribe("../recordingabuamrah.mp3")
print(result["text"])
