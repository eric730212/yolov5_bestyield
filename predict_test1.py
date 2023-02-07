import torch
import matplotlib.pyplot as plt
from models.common import DetectMultiBackend
from utils.torch_utils import select_device, smart_inference_mode

device = select_device(0)
model = DetectMultiBackend('runs/train/exp13/weights/best.pt', device=device, dnn=False, data='data/CustomData2.yaml',
                           fp16=False)
img = './dataset2/images/1.jpg'  # or file, Path, PIL, OpenCV, numpy, list
results = model(img)
fig, ax = plt.subplots(figsize=(1600, 1200))
ax.imshow(results.render()[0])
plt.show()
