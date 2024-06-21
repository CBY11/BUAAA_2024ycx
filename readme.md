python train.py --weights weights/yolov5s.pt  --cfg models/yolov5s.yaml  --data data/myvoc.yaml --epoch 20 --batch-size 4 --img 640   --device 0

python detect.py --weights runs/train/exp13/weights/best.pt --source ./data/test/img.png
