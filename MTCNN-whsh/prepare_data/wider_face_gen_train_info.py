import os
info_file = "wider_face_train.txt"
train_gt = "wider_face_train_bbx_gt.txt"
with open(train_gt, 'r') as f:
    gts = f.readlines()
count = len(gts)
print("there are %d records in gt file"%count)

outstr = ""
fw = open(info_file, 'w')
cnt = 0
for gt in gts:
    gt = gt.strip()
    if(gt.find("jpg")>0):
        cnt+=1
        if(len(outstr)>0):
            fw.write('%s\n'%(outstr))
            #print("out string = ", outstr)
            outstr=gt
            #print("one record has been processed!!")
        else:
            outstr=gt
            continue
    else:
        if(len(gt)<8):
            continue
        else:
            values = gt.split(" ")
            #print("gt = ",gt)
            if(int(values[7])==0):
                if(int(values[2]) > 0):
                    v0 = values[0]
                    v2 = values[2]
                else:
                    v0 = int(values[0]) + int(values[2])
                    if(v0<0):
                        continue
                    else:
                        v0 = str(v0)
                        v2 = str(0-int(values[2]))
                if(int(values[3]) > 0):
                    v1 = values[1]
                    v3 = values[3]
                else:
                    v1 = int(values[1]) + int(values[3])
                    if(v1<0):
                        continue
                    else:
                        v1 = str(v1)
                        v3 = str(0-int(values[3]))
                outstr = outstr + " " + v0 + " " + v1 + " " + v2 + " " + v3
            else:
                continue
fw.write('%s'%(outstr))
fw.flush()
fw.close()
print("there are %d images after processed.."%cnt)
print("finished..")