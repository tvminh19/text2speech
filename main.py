import subprocess

# Read content from data.txt
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Define the command to generate the voice file
command = f'edge-tts --voice vi-VN-HoaiMyNeural --text "{content}" --write-media output.mp3'

# Execute the command using subprocess
subprocess.run(command, shell=True)
