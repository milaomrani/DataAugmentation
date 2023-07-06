import os 
import argparse
import subprocess

import logging
import threading
import time

def thread_function(img, dst):
    logging.info("Thread %s: starting", img)
    # E:\C++_project\DataAugmentation\build\Debug\Data_Augmentation
    cmd = ['.\Debug\Data_Augmentation ', img, dst]
    print(cmd)
    # print(f" sub process is: {subprocess.call(cmd)}")
    subprocess.call(cmd)
    logging.info("Thread %s: finishing", img)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    #logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="Path to the src images")
    parser.add_argument("--dst", required=True, help="Path to the destination images")
    args = parser.parse_args()

    src_folder = args.src
    dst_folder = args.dst

    images = os.listdir(src_folder)

    num_threads = 4  # Specify the number of threads to use
    num_threads = min(num_threads, os.cpu_count())  # Limit to available CPU cores


    threads = list()

    for i in range(num_threads):
        for j in range(i, len(images), num_threads):
            img = images[j]
            img_path = os.path.join(src_folder, img)
            dst_path = os.path.join(dst_folder, img)
            logging.info("Main     : create and start thread for %s.", img)
            x = threading.Thread(target=thread_function, args=(img_path, dst_path))
            threads.append(x)
            x.start()
    

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)