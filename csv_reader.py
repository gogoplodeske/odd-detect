import pandas as pd
import os
from imageio import imread
import numpy as np
from matplotlib import pyplot as plt
import cv2
file_headers = ["# Frame", " x(0-1024)", " y(0-1024)", " obj id", " bounding size(0-1024^2)",
                " sequence(may be normalized)", " num objects", " current_time", " current_milli"]

header = ["frame", "x", "y", "obj_id", "bounding_size",
          "sequence", "num_objects", "current_time", "current_milli"]
color_list = [[0, 0, 0], [255, 255, 255], [0, 255, 0], [255, 0, 0], [0, 0, 255], [0, 0, 0], [255, 255, 255],
              [0, 255, 0], [255, 0, 0], [0, 0, 255]]
prev_point = {}

def read_directory(path):
    for root, dirs, files in os.walk(path):
        files.sort()
        yield from files


def read_csv(file):
    # chunksize = 1
    # with open(file, newline='') as csvfile:
    #     for chunk in pd.read_csv(csvfile, header=3, usecols=file_headers, chunksize=chunksize):
    #         yield chunk
    with open(file, newline='') as csvfile:
        df = pd.read_csv(csvfile, header=3, usecols=file_headers)
        df.columns = header
        return df


if __name__ == "__main__":
    # directory = read_directory("huji2.1")
    # data = next(directory)
    #
    # print(data)
    # df = read_csv("huji2.1/" + data)
    # print(next(df))
    # print(next(df))
    cHours = 0
    starthour = 5
    endhour =8

    image = cv2.imread("base.png")
    print(image.shape)
    # print(image[0,0])
    num_of_files = len(os.listdir(r'C:\Users\RENT\oddetect\huji2.1'))
    print(num_of_files)
    directory = read_directory("huji2.1")
    for i in range(10):
        data = next(directory)


        #print(data)
        df = read_csv("huji2.1/" + data)
        print(list(df.columns))
        print(df.head(10))
        for index, row in df.iterrows():
            x = int(row["x"])
            y = int(row["y"])
            obj_id = int(row["obj_id"])
            #print(obj_id)

            c = obj_id % 10
            key = str(row["obj_id"]) + '_' + str(i)
            curr_time = row["current_time"].split(' ')
            print(curr_time)
            time = curr_time[4]
            hour = int(time.split(':')[0])

            if ( cHours==1 and hour >= starthour and hour<endhour):
                print(time)
                print(hour)

                if key in prev_point:
                    point = prev_point[key]
                    itX = (1 if x <= point[0] else -1 )
                   # minX = (point[0] if x >= point[0] else x )
                    itY = (1 if y <= point[1] else -1)
                    #minY = (point[1] if y >= point[1] else y)
                    image = cv2.line(image, (x,y), tuple(point), tuple(color_list[c]), 2)
                    #image[x:point[0]:itX, y:point[1]:itY, 0:3] = color_list[obj_id]
                    prev_point[key] = [x, y]

                else:
                    image[x - 2:x + 2, y - 2:y + 2, 0:3] = color_list[c]
                    prev_point[key]=[x,y]
                #print(prev_point)
   # print( prev_point)
    plt.imshow(image)
    plt.show()




    # print(row["frame"])
    # break
# obj_id, x, y =
