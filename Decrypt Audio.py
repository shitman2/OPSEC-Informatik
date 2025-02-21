import wave

def bin_to_text(binary_string):
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if char != '11111110')

def decode_audio(audio_path):
    with wave.open(audio_path, 'rb') as audio:
        frames = list(audio.readframes(audio.getnframes()))

    binary_message = ''
    for sample in frames:
        binary_message += str(sample & 1)  # Extract LSB

        if binary_message[-16:] == '1111111111111110':
            break

    return bin_to_text(binary_message[:-16])  # Remove the end marker and convert to text

# Example Usage
hidden_message = decode_audio('encoded.wav')
print("Decoded Message:", hidden_message)
