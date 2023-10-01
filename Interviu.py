# Script 1: Deschide un videoclip preselectat din youtube

# import time
# import soundfile as sf
# import cv2
# import sounddevice as sd
# import numpy as np
# import pyautogui
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import threading
# import os
#
# # Director pentru stocarea fisierului sound_level.txt
# OUTPUT_DIRECTORY = "output_data"
#
# if not os.path.exists(OUTPUT_DIRECTORY):
#     os.makedirs(OUTPUT_DIRECTORY)
#
# OUTPUT_FILE_NAME = os.path.join(OUTPUT_DIRECTORY, "Inrg_Ecran_Video.wav")
# SOUND_LEVEL_FILE = os.path.join(OUTPUT_DIRECTORY, "sound_level.txt")
#
# SAMPLE_RATE = 98000
# record_seconds = 30
#
# def rms_flat(a):
#     return np.sqrt(np.mean(np.absolute(a)**2))
#
# def record_audio():
#     print("Recording audio...")
#     # virtual_audio_device_name = 'CABLE OUTPUT(VB-Audio Virtual Cable)'
#     # input_device_id = None
#     # for i, device_info in enumerate(sd.query_devices()):
#     #     if device_info['name'] == virtual_audio_device_name:
#     #         input_device_id = i
#     #         break
#     # if input_device_id is None:
#     #     print(f"Virtual audio device '{virtual_audio_device_name}' not found.")
#     #     return
#
#     channels = 1
#     audio_data = sd.rec(int(SAMPLE_RATE * record_seconds), samplerate=SAMPLE_RATE, channels=channels)
#     sd.wait()  # Wait for the recording to finish
#     audio_data = audio_data.flatten()
#
#     aw_spl = 20 * np.log10(rms_flat(audio_data)) - 20 * np.log10(32767)
#
#     try:
#         with open(SOUND_LEVEL_FILE, "w") as f:
#             f.write(f"Decibels: {aw_spl:.2f} dB")
#         print(f"Sound level written to {SOUND_LEVEL_FILE}")
#     except Exception as e:
#         print(f"Error writing sound level to file: {str(e)}")
#
#     sf.write(file=OUTPUT_FILE_NAME, data=audio_data, samplerate=SAMPLE_RATE)
#     print(f"Finished recording audio. Decibels: {aw_spl:.2f} dB")
#
# def record_video():
#     SCREEN_SIZE = tuple(pyautogui.size())
#     fourcc = cv2.VideoWriter_fourcc(*"XVID")
#     fps = 20.0
#     out = cv2.VideoWriter("Inrg_Ecran_Video.avi", fourcc, fps, (SCREEN_SIZE))
#
#     print("Recording screen..")
#     for i in range(int(record_seconds * fps)):
#         img = pyautogui.screenshot()
#         frame = np.array(img)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         out.write(frame)
#     print("Finished recording screen")
#     cv2.destroyAllWindows()
#     out.release()
#
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get('https://www.youtube.com/watch?v=RhUzG8_67qc')
# print(driver.title)
# print(driver.current_url)
#
# wait = WebDriverWait(driver, 10)
# accept_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Accept all']")))
#
# driver.execute_script("arguments[0].scrollIntoView();", accept_all_button)
# driver.execute_script("arguments[0].click();", accept_all_button)
#
# time.sleep(15)
#
# audio_thread = threading.Thread(target=record_audio)
# video_thread = threading.Thread(target=record_video)
# audio_thread.start()
# video_thread.start()
# audio_thread.join()
# video_thread.join()
#
# driver.quit()

# Script 2 : Deschide un video oarecare de pe youtube
import time
import soundfile as sf
import cv2
import sounddevice as sd
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import os
import random

OUTPUT_DIRECTORY = "output_data"

if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

OUTPUT_FILE_NAME = os.path.join(OUTPUT_DIRECTORY, "Inrg_Ecran.wav")
SOUND_LEVEL_FILE = os.path.join(OUTPUT_DIRECTORY, "sound_level.txt")

SAMPLE_RATE = 98000
record_seconds = 30

def rms_flat(a):
    return np.sqrt(np.mean(np.absolute(a)**2))

def record_audio():
    print("Recording audio...")
    channels = 1
    audio_data = sd.rec(int(SAMPLE_RATE * record_seconds), samplerate=SAMPLE_RATE, channels=channels)
    sd.wait()
    audio_data = audio_data.flatten()

    aw_spl = 20 * np.log10(rms_flat(audio_data)) - 20 * np.log10(32767)

    try:
        with open(SOUND_LEVEL_FILE, "w") as f:
            f.write(f"Decibels: {aw_spl:.2f} dB")
        print(f"Sound level written to {SOUND_LEVEL_FILE}")
    except Exception as e:
        print(f"Error writing sound level to file: {str(e)}")

    sf.write(file=OUTPUT_FILE_NAME, data=audio_data, samplerate=SAMPLE_RATE)
    print(f"Finished recording audio. Decibels: {aw_spl:.2f} dB")

def record_video():
    SCREEN_SIZE = tuple(pyautogui.size())
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 20.0
    out = cv2.VideoWriter("Inrg_Ecran_Video.avi", fourcc, fps, (SCREEN_SIZE))

    print("Recording screen..")
    for i in range(int(record_seconds * fps)):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    print("Finished recording screen")
    cv2.destroyAllWindows()
    out.release()

def open_random_video():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://www.youtube.com/')
    print(driver.title)
    print(driver.current_url)

    wait = WebDriverWait(driver, 10)
    accept_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Accept all']")))

    driver.execute_script("arguments[0].scrollIntoView();", accept_all_button)
    driver.execute_script("arguments[0].click();", accept_all_button)

    time.sleep(15)

    try:
        search_input = driver.find_element(By.NAME, "search_query")
        search_input.clear()
    except:
        pass

    recommended_videos = driver.find_elements(By.XPATH, "//a[contains(@href, '/watch?')]")
    if recommended_videos:
        random_video = random.choice(recommended_videos)
        driver.execute_script("arguments[0].scrollIntoView();", random_video)
        driver.execute_script("window.scrollBy(0, -150);")
        random_video.click()
        time.sleep(5)


        audio_thread = threading.Thread(target=record_audio)
        video_thread = threading.Thread(target=record_video)

        audio_thread.start()
        video_thread.start()

        audio_thread.join()
        video_thread.join()
    else:
        print("No recommended videos found.")

    driver.quit()

if __name__ == "__main__":
    open_random_video()
