import subprocess
import os
import argparse

def convert_sound(input, output=None):
    if output is None:
        output = os.path.splitext(input)[0] + ".ogg"
    else:
        output = os.path.splitext(input)[0] + "." + output
    result = subprocess.run([
        "ffmpeg", "-y", "-i", input, output
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Converted {input} to {output}")
        os.remove(input)  # Remove the original WAV file
        print(f"Removed original file: {input}")
    else:
        print("Error converting file:")
        print(result.stderr)

def recursive_convert(args):
    allowed_formats = tuple(args.format)
    if args.output in allowed_formats:
        raise ValueError(f"Specified output format '{args.output}' is included in allowed input formats: {allowed_formats}. Aborting recursive conversion.")


    print(f"Recursively converting {allowed_formats} files in:", args.input)
    if os.path.isdir(args.input):
        for root, _, files in os.walk(args.input):
            print(f"Searching in directory: {root}")
            for file in files:
                if file.endswith(allowed_formats):
                    input_file = os.path.join(root, file)
                    convert_sound(input_file, args.output)

    elif args.input.endswith(allowed_formats):
        convert_sound(args.input)
    else:
        print(f"Unsupported file type: {args.input}")

def main():
    parser = argparse.ArgumentParser(description="Convert WAV files to OGG format.")
    parser.add_argument("input", help="Input WAV file or directory containing WAV files")

    parser.add_argument("-o", "--output", default="ogg", help="Output OGG file (optional, defaults to input filename with .ogg extension)")

    parser.add_argument("-f", "--format", default=["wav"], type=str, nargs="*", help="Input file formats (default is WAV) to be used with recursive conversion")

    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively search for WAV files in directories")
    args = parser.parse_args()

    if args.recursive:
        recursive_convert(args)
    else:
        convert_sound(args.input)




if __name__ == "__main__":
    main()
