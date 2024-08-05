# -*- coding: utf-8 -*-
import os.path
import os
import sys
import subprocess
from pathlib import Path

FFMPEG = "D:/ffmpeg-7.0.2-essentials_build/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe"

def is_jpg(filename):
    """Checks if the given filename has a JPG extension (case-insensitive).
    Args:
            filename: The filename to check.
    Returns:
            True if the filename has a JPG extension, False otherwise.
    """
    _, ext = os.path.splitext(filename.lower())
    return ext == ".jpg"

def fetch_cover_from_audio(cover_path, mp3_path):
    print(f"\n===Trying to get the cover from the mp3 file===")
    ffmpeg_command = [
        # "ffmpeg",
        FFMPEG,
        "-i", mp3_path,
        "-an",
        "-c:v", "copy",
        cover_path,
    ]
    print("====> Running ffmpeg command:")
    print(subprocess.list2cmdline(ffmpeg_command))
    cmds_raw = f"ffmpeg -i '{mp3_path}' -an -c:v copy '{cover_path}'" 
    os.system("echo !!!!!!!!!!!!!!!!!!!!")
    # os.system("D:/ffmpeg-7.0.2-essentials_build/ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe --help")
    # os.system(cmds_raw)
    subprocess.run(ffmpeg_command, check=True, text=True, encoding='utf-8')

def convert_to_mp4(cover_path, mp3_path, output_path):
    """Converts an image (assumed JPG) and an MP3 file to an MP4 container.

    Args:
            cover_path: Path to the image file (JPG).
            mp3_path: Path to the MP3 audio file.
            output_path: Path to the output MP4 file.

    Raises:
            ValueError: If the cover file is not a JPG.
    """
    if not is_jpg(cover_path):
        raise ValueError(f"Cover file '{cover_path}' must be a JPG image.")

    if not os.path.exists(cover_path):
        notes = "Missing Cover!"
        print(f"{notes:=^30}")
        fetch_cover_from_audio(cover_path,mp3_path)

    print(f"\tCOVER: {cover_path}")
    print(f"\tAUDIO: {mp3_path}")
    print(f"\tOUTPUT: {output_path}")

    # Improved command construction with string formatting
    ffmpeg_command = [
        # "ffmpeg",
        FFMPEG,
        "-loop", "1",
        "-i", cover_path,
        "-i", mp3_path,
        "-c:a", "copy",
        "-c:v", "libx264",
        "-shortest", output_path,
    ]
    subprocess.run(ffmpeg_command, check=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: simple-convert.py <mp3_file>")
        sys.exit(1) 

    mp3_path = Path(sys.argv[1])
    song_name = mp3_path.stem
    print(f"=====> {song_name} detected")
    cover_path = mp3_path.with_suffix('.jpg')
    output_path = mp3_path.with_suffix('.mp4')

    convert_to_mp4(str(cover_path), str(mp3_path), str(output_path))
