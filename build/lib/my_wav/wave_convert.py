import subprocess
import os
import argparse

def convert_wav_to_ogg(wav_path, ogg_path=None):
    if ogg_path is None:
        ogg_path = os.path.splitext(wav_path)[0] + ".ogg"
    result = subprocess.run([
        "ffmpeg", "-y", "-i", wav_path, ogg_path
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Converted {wav_path} to {ogg_path}")
        os.remove(wav_path)  # Remove the original WAV file
        print(f"Removed original file: {wav_path}")
    else:
        print("Error converting file:")
        print(result.stderr)

def recursive_convert(input_path):
    print("Recursively converting WAV files in:", input_path)
    if os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            print(f"Searching in directory: {root}")
            for file in files:
                if file.endswith(".wav"):
                    wav_file = os.path.join(root, file)
                    convert_wav_to_ogg(wav_file)

    elif input_path.endswith(".wav"):
        convert_wav_to_ogg(input_path)
    else:
        print(f"Unsupported file type: {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert WAV files to OGG format.")
    parser.add_argument("input", help="Input WAV file or directory containing WAV files")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively search for WAV files in directories")
    args = parser.parse_args()
    if args.recursive:
        recursive_convert(args.input)
    else:
        convert_wav_to_ogg(args.input)



    # import sys
    # if len(sys.argv) < 2:
    #     print("Usage: python wave_convert.py input.wav [output.ogg]")
    # else:
    #     wav_file = sys.argv[1]
    #     ogg_file = sys.argv[2] if len(sys.argv) > 2 else None
    #     convert_wav_to_ogg(wav_file, ogg_file)
