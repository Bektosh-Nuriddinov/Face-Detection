___
# Face-Detection
This project can detect human face using comera.The project is based on artificial intelligence, written in [Python](https://www.python.org/) programming language, and the model training part uses [YOLOV8](https://github.com/ultralytics/ultralytics) provided by ultralytics, and the interface is made using [Streamlit](https://docs.streamlit.io/).<br>
#### Datasets
You can get the datasets used in model training through the link below -> [Link](https://app.roboflow.com/ds/IcTG6m9LEy?key=WGrMr9XBR9)
<br>
| Dataset                                                                                     | Total<br><sup>Images | Validation<sup>val<br>Images | Test<br><sup>Images |
| ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------------------------ |
| [Link](https://app.roboflow.com/ds/IcTG6m9LEy?key=WGrMr9XBR9) | 640                   | 33.6                 | 408.5                          |
The dataset consists of a total of 5741 labeled images.5022 images for train,477 images for validation ,442 images for test are   splited.
  
#### Model Training
YOLOv8m was used during model training. You can see its parameters below.<br>
| Model                                                                                     | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m-oiv7.pt) | 640                   | 33.6                 | 408.5                          | 2.26                                | 26.2               | 80.6              |
<br>
100 epoch have passed in the sample train process. Accuracy is 84.2%.This was a trial project, it was trained in fewer periods. If you need higher accuracy, increase the epoch and you will achieve the goal.

