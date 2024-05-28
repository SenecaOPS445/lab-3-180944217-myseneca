#!/usr/bin/env python3
'''Lab 3 script to return free disk space on Linux root directory'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
    df_process = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    grep_process = subprocess.Popen(['grep', '/$'], stdin=df_process.stdout, stdout=subprocess.PIPE)
    awk_process = subprocess.Popen(['awk', '{print $4}'], stdin=grep_process.stdout, stdout=subprocess.PIPE)
    df_process.stdout.close()  # Close the stdout of df_process as it's no longer needed

    # Get the output of the awk command
    output, _ = awk_process.communicate()

    # Return the output as a string with newline characters stripped
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
