import cv2


def read2save():
    cap = cv2.VideoCapture('C_13_3.mp4') #读入的视频是15帧的
    #输出path
    frame_count = 0
    cap1 = cv2.VideoCapture('output.mp4')
    print(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    print(cap1.get(cv2.CAP_PROP_FPS))
    print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(cap.get(cv2.CAP_PROP_FPS))
    video_write = cv2.VideoWriter('output.mp4',
                                  cv2.VideoWriter_fourcc(*'mp4v'),
                                  int(15), #这个决定了播放速度的问题  没有减少帧的取样。依然每帧都会取的
                                  (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                   round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

    while True:
        ret,frame = cap.read()
        print(cap.isOpened())
        if ret is True:
            frame_count = frame_count + 1
            cv2.imshow('x',frame)
            video_write.write(frame)
            cv2.waitKey(1) #这个只是控制显示的  或者这一循环走完需要等待多久
        else:
            print(frame_count)
            print('is end')
            break

if __name__ == "__main__":
    print('start')
    read2save()
