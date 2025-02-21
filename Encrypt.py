import wave
import numpy as np

def text_to_bin(text):
    return ''.join(format(ord(char), '08b') for char in text)

def encode_audio(audio_path, message, output_path):
    with wave.open(audio_path, 'rb') as audio:
        params = audio.getparams()
        frames = np.frombuffer(audio.readframes(audio.getnframes()), dtype=np.int16)

    binary_message = text_to_bin(message) + '1111111111111110'
    data_index = 0

    for i in range(len(frames)):
        if data_index < len(binary_message):
            frames[i] = frames[i] & ~1 | int(binary_message[data_index])
            data_index += 1
        else:
            break

    with wave.open(output_path, 'wb') as encoded_audio:
        encoded_audio.setparams(params)
        encoded_audio.writeframes(frames.tobytes())

    print("Message encoded successfully!")

# Change the text to whatever ur stuff is called
encode_audio('input.wav', 'Hidden Message', 'encoded.wav')
