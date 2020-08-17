def autosub(file_string):
    import os
    import subprocess
    print(os.getcwd())
    subprocess.run([".\\autosub", "-S","en-US","-i", file_string])
    subprocess.run(["python", "subtitle_to_text.py","test.en-us.srt"])