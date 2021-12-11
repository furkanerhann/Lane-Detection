# changing the camera angle will require you to change many variables here!
import cv2 as cv
import numpy as np
cap = cv.VideoCapture('test.mp4')
roi = [(0, 600), (800, 600), (440, 380), (360, 380)]
class LaneDetection:
    def bubblesort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    def slope2alpha(s):
        slope = s * 1000
        if slope >= 0 and slope < 982: # 0-44
            if slope < 2500: # 0-14
                if slope < 5:
                    alpha = 0
                elif slope < 25:
                    alpha = 1
                elif slope < 45:
                    alpha = 2
                elif slope < 60:
                    alpha = 3
                elif slope < 75:
                    alpha = 4
                elif slope < 95:
                    alpha = 5
                elif slope < 110:
                    alpha = 6
                elif slope < 130:
                    alpha = 7
                elif slope < 142:
                    alpha = 8
                elif slope < 165:
                    alpha = 9
                elif slope < 181:
                    alpha = 10
                elif slope < 199:
                    alpha = 11
                elif slope < 216:
                    alpha = 12
                elif slope < 235:
                    alpha = 13
                else:
                    alpha = 14
            elif slope < 565: # 15-29
                if slope < 273:
                    alpha = 15
                elif slope < 295:
                    alpha = 16
                elif slope < 315:
                    alpha = 17
                elif slope < 335:
                    alpha = 18
                elif slope < 355:
                    alpha = 19
                elif slope < 373:
                    alpha = 20
                elif slope < 393:
                    alpha = 21
                elif slope < 414:
                    alpha = 22
                elif slope < 435:
                    alpha = 23
                elif slope < 455:
                    alpha = 24
                elif slope < 476:
                    alpha = 25
                elif slope < 498:
                    alpha = 26
                elif slope < 515:
                    alpha = 27
                elif slope < 545:
                    alpha = 28
                else:
                    alpha = 29
            else: # 30-44
                if slope < 584:
                    alpha = 30
                elif slope < 612:
                    alpha = 31
                elif slope < 627:
                    alpha = 32
                elif slope < 665:
                    alpha = 33
                elif slope < 688:
                    alpha = 34
                elif slope < 713:
                    alpha = 35
                elif slope < 739:
                    alpha = 36
                elif slope < 767:
                    alpha = 37
                elif slope < 795:
                    alpha = 38
                elif slope < 82:
                    alpha = 39
                elif slope < 855:
                    alpha = 40
                elif slope < 885:
                    alpha = 41
                elif slope < 916:
                    alpha = 42
                elif slope < 948:
                    alpha = 43
                else:
                    alpha = 44
        elif slope >= 982: # 45-90
            if slope < 1700: # 45-59
                if slope < 1017:
                    alpha = 45
                elif slope < 1043:
                    alpha = 46
                elif slope < 1091:
                    alpha = 47
                elif slope < 1130:
                    alpha = 48
                elif slope < 1170:
                    alpha = 49
                elif slope < 1210:
                    alpha = 50
                elif slope < 1250:
                    alpha = 51
                elif slope < 1300:
                    alpha = 52
                elif slope < 1350:
                    alpha = 53
                elif slope < 1400:
                    alpha = 54
                elif slope < 1450:
                    alpha = 55
                elif slope < 1510:
                    alpha = 56
                elif slope < 1570:
                    alpha = 57
                elif slope < 1632:
                    alpha = 58
                else:
                    alpha = 59
            elif slope < 3600: # 60-74
                if slope < 1768:
                    alpha = 60
                elif slope < 1842:
                    alpha = 61
                elif slope < 1920:
                    alpha = 62
                elif slope < 2000:
                    alpha = 63
                elif slope < 2100:
                    alpha = 64
                elif slope < 2200:
                    alpha = 65
                elif slope < 2300:
                    alpha = 66
                elif slope < 2400:
                    alpha = 67
                elif slope < 2520:
                    alpha = 68
                elif slope < 2660:
                    alpha = 69
                elif slope < 2820:
                    alpha = 70
                elif slope < 3000:
                    alpha = 71
                elif slope < 3100:
                    alpha = 72
                elif slope < 3300:
                    alpha = 73
                else:
                    alpha = 74
            else: # 75-90
                if slope < 3860:
                    alpha = 75
                elif slope < 4160:
                    alpha = 76
                elif slope < 4510:
                    alpha = 77
                elif slope < 4920:
                    alpha = 78
                elif slope < 5400:
                    alpha = 79
                elif slope < 6000:
                    alpha = 80
                elif slope < 6700:
                    alpha = 81
                elif slope < 7600:
                    alpha = 82
                elif slope < 8800:
                    alpha = 83
                elif slope < 10500:
                    alpha = 84
                elif slope < 12900:
                    alpha = 85
                elif slope < 16600:
                    alpha = 86
                elif slope < 23800:
                    alpha = 87
                elif slope < 42900:
                    alpha = 88
                else:
                    alpha = 89
        elif slope > -982 and slope < 0: # 136-180
            if slope > -250: # 166-180
                if slope > -5:
                    alpha = 180
                elif slope > -25:
                    alpha = 179
                elif slope > -45:
                    alpha = 178
                elif slope > -60:
                    alpha = 177
                elif slope > -75:
                    alpha = 176
                elif slope > -95:
                    alpha = 175
                elif slope > -110:
                    alpha = 174
                elif slope > -130:
                    alpha = 173
                elif slope > -142:
                    alpha = 172
                elif slope > -165:
                    alpha = 171
                elif slope > -181:
                    alpha = 170
                elif slope > -199:
                    alpha = 169
                elif slope > -216:
                    alpha = 168
                elif slope > -235:
                    alpha = 167
                else:
                    alpha = 166
            elif slope > -565: # 151-165
                if slope > -273:
                    alpha = 165
                elif slope > -295:
                    alpha = 164
                elif slope > -315:
                    alpha = 163
                elif slope > -335:
                    alpha = 162
                elif slope > -355:
                    alpha = 161
                elif slope > -373:
                    alpha = 160
                elif slope > -393:
                    alpha = 159
                elif slope > -414:
                    alpha = 158
                elif slope > -435:
                    alpha = 157
                elif slope > -455:
                    alpha = 156
                elif slope > -476:
                    alpha = 155
                elif slope > -498:
                    alpha = 154
                elif slope > -515:
                    alpha = 153
                elif slope > -545:
                    alpha = 152
                else:
                    alpha = 151
            else: # 136-150
                if slope > -584:
                    alpha = 150
                elif slope > -612:
                    alpha = 149
                elif slope > -627:
                    alpha = 148
                elif slope > -665:
                    alpha = 147
                elif slope > -688:
                    alpha = 146
                elif slope > -713:
                    alpha = 145
                elif slope > -739:
                    alpha = 144
                elif slope > -767:
                    alpha = 143
                elif slope > -795:
                    alpha = 142
                elif slope > -820:
                    alpha = 141
                elif slope > -855:
                    alpha = 140
                elif slope > -885:
                    alpha = 139
                elif slope > -916:
                    alpha = 138
                elif slope > -948:
                    alpha = 137
                else:
                    alpha = 136
        else: # 91-135
            if slope > -1700: # 121-135
                if slope > -1017:
                    alpha = 135
                elif slope > -1043:
                    alpha = 134
                elif slope > -1091:
                    alpha = 133
                elif slope > -1130:
                    alpha = 132
                elif slope > -1170:
                    alpha = 131
                elif slope > -1210:
                    alpha = 130
                elif slope > -1250:
                    alpha = 129
                elif slope > -1300:
                    alpha = 128
                elif slope > -1350:
                    alpha = 127
                elif slope > -1400:
                    alpha = 126
                elif slope > -1450:
                    alpha = 125
                elif slope > -1510:
                    alpha = 124
                elif slope > -1570:
                    alpha = 123
                elif slope > -1632:
                    alpha = 122
                else:
                    alpha = 121
            elif slope > -3600: # 106-120
                if slope > -1768:
                    alpha = 120
                elif slope > -1842:
                    alpha = 119
                elif slope > -1920:
                    alpha = 118
                elif slope > -2000:
                    alpha = 117
                elif slope > -2100:
                    alpha = 116
                elif slope > -2200:
                    alpha = 115
                elif slope > -2300:
                    alpha = 114
                elif slope > -2400:
                    alpha = 113
                elif slope > -2520:
                    alpha = 112
                elif slope > -2660:
                    alpha = 111
                elif slope > -2820:
                    alpha = 110
                elif slope > -3000:
                    alpha = 109
                elif slope > -3100:
                    alpha = 108
                elif slope > -3300:
                    alpha = 107
                else:
                    alpha = 106
            else: # 91-105
                if slope > -3860:
                    alpha = 105
                elif slope > -4160:
                    alpha = 104
                elif slope > -4510:
                    alpha = 103
                elif slope > -4920:
                    alpha = 102
                elif slope > -5400:
                    alpha = 101
                elif slope > -6000:
                    alpha = 100
                elif slope > -6700:
                    alpha = 99
                elif slope > -7600:
                    alpha = 98
                elif slope > -8800:
                    alpha = 97
                elif slope > -10500:
                    alpha = 96
                elif slope > -12900:
                    alpha = 95
                elif slope > -16600:
                    alpha = 94
                elif slope > -23800:
                    alpha = 93
                elif slope > -42900:
                    alpha = 92
                else:
                    alpha = 91
        if alpha > 90:
            alpha -= 180
        return alpha
    def collectlines(mask):
        lines = cv.HoughLinesP(mask, 2, np.pi / 180, 20, np.array([]), minLineLength=25, maxLineGap=0)
        slopes = []
        new_lines = []
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                if x2 - x1 == 0.:
                    slope = 999.
                else:
                    slope = (y2 - y1) / (x2 - x1)
                if abs(slope) > 0.5:
                    slopes.append(slope)
                    new_lines.append(line)
        return new_lines
    def separatelines(lines, center):
        slopes = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 - x1 == 0.:
                slope = 999.
            else:
                slope = (y2 - y1) / (x2 - x1)
            slopes.append(slope)
        right_lines = []
        left_lines = []
        for i, line in enumerate(lines):
            x1, y1, x2, y2 = line[0]

            if slopes[i] > 0 and x1 > center and x2 > center:
                right_lines.append(line)
            elif slopes[i] < 0 and x1 < center and x2 < center:
                left_lines.append(line)
        return left_lines, right_lines
    def compresslines(lines):
        if len(lines) == 1:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                slope = (y2 - y1) / (x2 - x1)
                x = (x1+x2)/2
                y = (y1+y2)/2
                alpha = LaneDetection.slope2alpha(slope)
                return x, y, slope, alpha
        else:
            slopes = []
            for line in lines:
                x1, y1, x2, y2 = line[0]
                slope = (y2 - y1) / (x2 - x1)
                slopes.append(slope)
            LaneDetection.bubblesort(slopes)
            mid = int(len(slopes)/2)
            median = slopes[mid]
            mean = 0
            for s in slopes:
                mean += s
            mean = mean/len(slopes)
            median_alpha = LaneDetection.slope2alpha(median)
            mean_alpha = LaneDetection.slope2alpha(mean)
            if median_alpha > mean_alpha - 10 and median_alpha < mean_alpha + 10:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    slope = (y2 - y1) / (x2 - x1)
                    alpha = LaneDetection.slope2alpha(slope)
                    x = (x1 + x2) / 2
                    y = (y1 + y2) / 2
                    if slope == median:
                        return x, y, slope, alpha
            else:
                new_lines = []
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    slope = (y2 - y1) / (x2 - x1)
                    if slope != median:
                        new_lines.append(line)
                x, y, s, a = LaneDetection.compresslines(new_lines)
                return x, y, s, a
    def drawline(frame, x, y, slope, miny, maxy):
        minx = int(x + ((miny-y)/slope))
        maxx = int(x - ((y-maxy)/slope))
        cv.line(frame, (minx,miny), (maxx, maxy), (255, 255, 0), 10)
        return frame
    def getway(way):
        if way < -50:
            return "Left"
        elif way < -37:
            return "A Little bit Left"
        elif way <= 37:
            return "Forward"
        elif way <= 50:
            return "A Little bit Right"
        else:
            return "Right"
    def start_process(frame):
        blur = cv.GaussianBlur(frame, (5, 5), 1)
        gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
        th, bw = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
        mask = np.zeros_like(bw)
        match_mask_color = (255,)
        cv.fillPoly(mask, np.array([roi], np.int32), match_mask_color)
        mask = cv.bitwise_and(bw, mask)
        lines = LaneDetection.collectlines(mask)
        l_lines, r_lines = LaneDetection.separatelines(lines, 400)
        draw_left = True
        draw_right = True
        if len(l_lines) > 0:
            lx, ly, ls, la = LaneDetection.compresslines(l_lines)
        else:
            draw_left = False
            la = 0
        if len(r_lines) > 0:
            rx, ry, rs, ra = LaneDetection.compresslines(r_lines)
        else:
            draw_right = False
            ra = 0
        if draw_left:
            frame = LaneDetection.drawline(frame, lx, ly, ls, 380, 600)
        if draw_right:
            frame = LaneDetection.drawline(frame, rx, ry, rs, 380, 600)
        way = la+ra
        way = LaneDetection.getway(way)
        return frame, way
while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, (800, 600))
    if ret:
        frame, way = LaneDetection.start_process(frame)
        cv.imshow('frame', frame)
        print(way)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    else: break