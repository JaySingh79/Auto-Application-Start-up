import subprocess
import os
# def execute_kaggle():
#     # # Construct the command as a list for better handling.
#     # # Ensure Chrome's executable is in the PATH or provide its full path.
#     # command = ["start "
#     #     "chrome", 
#     #     '--profile-directory="Profile 3"', 
#     #     "https://www.kaggle.com/jaysingh79"
#     # ]
    
#     try:
#         os.system('start chrome --Profile-Directory="Profile 4" "https://www.kaggle.com/jaysingh79"')
#     except Exception as e:
#         print("Failed to launch Chrome:", e)


def execute_kaggle():
    subprocess.Popen(
        ["start", "chrome", "--Profile-Directory=Profile 4", "https://www.kaggle.com/jaysingh79"],
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


if __name__ == "__main__":
    execute_kaggle()
