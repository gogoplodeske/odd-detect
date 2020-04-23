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

monthes = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "June": 6, "July": 7, "Agu": 8, "Sept": 9, "Oct": 10,
           "Nov": 11, "Dec": 12}


class Track:
    def __init__(self, image, dir, size, starthour=0, endhour=24, C2=0, date1=None, date2=None, topleft=[0, 0],
                 bottonright=[1023, 1023]):
        self.image = image
        self.dir = dir
        self.starthour = starthour
        self.endhour = endhour
        self.c2 = C2
        self.date1 = np.array(date1)
        self.date2 = np.array(date2)
        self.topleft = np.array(topleft)
        self.bottonright = np.array(bottonright)
        self.size = size * size

    def read_directory(self):
        for root, dirs, files in os.walk(self.dir):
            files.sort()
            yield from files

    def read_csv(self, file):
        # chunksize = 1
        # with open(file, newline='') as csvfile:
        #     for chunk in pd.read_csv(csvfile, header=3, usecols=file_headers, chunksize=chunksize):
        #         yield chunk
        with open(file, newline='') as csvfile:
            df = pd.read_csv(csvfile, header=3, usecols=file_headers)
            df.columns = header
            return df

    def show(self):
        prev_point = {}
        starthour = self.starthour
        endhour = self.endhour
        image = self.image

        # image = cv2.imread("base.png")
        print(image.shape)
        num_of_files = len(os.listdir(self.dir))

        directory = self.read_directory()
        for i in range(10):
            data = next(directory)
            prev_point = {}

            # print(data)
            df = self.read_csv(os.path.join(self.dir, data))
            print(df.head(10))
            df = df[df['x'] > self.topleft[0]]
            df = df[df['y'] > self.topleft[1]]
            df = df[df['x'] < self.bottonright[0]]
            df = df[df['y'] < self.bottonright[1]]
            df = df[df['bounding_size'] < self.size]
            df =


            print("this is my thing to check \n")

            print(df['bounding_size'].dtype)
           # df = df[df['bounding_size']] < self.size
            for index, row in df.iterrows():
                x = int(row["x"])
                y = int(row["y"])
                obj_id = int(row["obj_id"])
                c = obj_id % 10
                key = str(row["obj_id"]) + '_' + str(i)
                curr_time = row["current_time"].split(' ')
                time = curr_time[4]
                hour = int(time.split(':')[0])
                month = monthes[curr_time[2]]
                day = int(curr_time[3])
                year = int(curr_time[5])
                datarray = np.array([day, month, year])
                strictly = ((self.date1 < datarray) & (datarray < self.date2))
                eq = ((self.date1 == datarray) | (datarray == self.date2))
                points = np.array([x, y])
                # maskarea = ((self.topleft <= points) &  (points <= self.bottonright))
                # size = int(row["bounding_size"])

                if (strictly[2] == True) or (eq[2] == True and strictly[1] == True) or (
                        eq[2] == True and eq[1] == True and (eq[0] == True or strictly[0] == True)):
                    if starthour <= hour and hour <= endhour:  # and np.all(maskarea) == True:
                        print(self.size)
                        if key in prev_point:
                            point = prev_point[key]
                            itX = (1 if x <= point[0] else -1)
                            # minX = (point[0] if x >= point[0] else x )
                            itY = (1 if y <= point[1] else -1)
                            # minY = (point[1] if y >= point[1] else y)
                            image = cv2.line(image, (x, y), tuple(point), tuple(color_list[c]), 2)
                            # image[x:point[0]:itX, y:point[1]:itY, 0:3] = color_list[obj_id]
                            prev_point[key] = [x, y]
                        else:
                            # image[x , y , :] = color_list[c]
                            prev_point[key] = [x, y]

        plt.imshow(image)
        plt.show()
