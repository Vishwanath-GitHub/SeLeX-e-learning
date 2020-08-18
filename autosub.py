def autosub(file_string, search_results):
    import os
    import subprocess
    subprocess.run([".\\autosub", "-S","en-US","-i", file_string])
    subprocess.run(["python", "subtitle_to_text.py",search_results + ".en-us.srt"])

