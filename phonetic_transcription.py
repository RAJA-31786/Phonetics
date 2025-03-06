import re
import subprocess  # To run performance_metrics.py automatically
from featuretable import features


# Function to transcribe input text to phonetics
def transcribe_word(text):
    transcription = []
    for char in text:
        if char in features:
            feature = features[char]
            transcription.append(f"{char}({feature['place']}, {feature['manner']}, {feature['voice']})")
        else:
            transcription.append(char)  # Print as-is for unsupported characters
    return ' '.join(transcription)


# Main function to handle user input and save transcription
def main():
    print("Phonetic Transcription System")
    print("Enter a word or sentence to transcribe (or type 'exit' to quit):")

    # Save transcriptions to a file
    with open("transcription_output.txt", "w") as file:
        while True:
            text = input("> ")
            if text.lower() == 'exit':
                break
            result = transcribe_word(text)
            print("Transcription:", result)
            # Save both predicted and correct transcription as the same
            file.write(f"{text}:{result}:{result}\n")

    print("\nTranscriptions saved to 'transcription_output.txt'.")
    print("Running performance metrics...\n")

    # Run performance_metrics.py automatically
    subprocess.run(["python", "performance_metrics.py"])


# Run the main function if executed directly
if __name__ == "__main__":
    main()

