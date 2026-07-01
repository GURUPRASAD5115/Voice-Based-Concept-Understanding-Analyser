from modules.audio_utils import extract_audio_features

audio_path = "audio/input/Recording.mp3"

features = extract_audio_features(audio_path)

print("Audio Feature Test")
print("------------------")
print(features)