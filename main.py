import subprocess
import os

def execute_kaggle():

    ## below is the code to open a certain link in your specific chrome profile
    ## you can add your required command to open directly.
    subprocess.Popen(
        ["start", "chrome", "--Profile-Directory=`Your Profile Number'", "your_link"],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


if __name__ == "__main__":
    execute_kaggle()
