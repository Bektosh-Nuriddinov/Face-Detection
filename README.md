___
## Face-Detection
This project can detect human face using comera.The project is based on artificial intelligence, written in [Python](https://www.python.org/) programming language, and the model training part uses [YOLOV8](https://github.com/ultralytics/ultralytics) provided by ultralytics, and the interface is made using [Streamlit](https://docs.streamlit.io/).<br>
### Datasets
You can get the datasets used in model training through the link below.
<br>
| Dataset                                                                                     | Total<br><sup>Images | Validation<sup><br>Images | Test<br><sup>Images |
| ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------------------------ |
| [dataset V6](https://app.roboflow.com/ds/IcTG6m9LEy?key=WGrMr9XBR9) | 5741                   | 477                 | 442                         |
<br>

### Model Training
YOLOv8m was used during model training. You can see its parameters below.<br>
| Model                                                                                     | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
| ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8m-oiv7.pt) | 640                   | 33.6                 | 408.5                          | 2.26                                | 26.2               | 80.6              |

<br>
100 epoch have passed in the sample train process. Accuracy is 84.2%.This was a trial project, it was trained in fewer periods. If you need higher accuracy, increase the epoch and you will achieve the goal.

### Install
#### Step 1
First, you must have the [Python](https://www.python.org/) programming language installed on your computer. If it is not installed, install it.
#### Step 2
Then download this project to your computer
#### Step 3
Go to the project file and install the requirements.
```bash
pip install -r requirements.txt
```
This is take some time.
### Usage
We have everything ready.<br>
Run the project:
```bash
streamlit run streamlit_app.py 
```
Congratulations. Now you can go to the browser and use the project.
<br>
## <div align="center">Contact</div>
<br>
<div align="center">
  <a href="https://github.com/Bektosh-Nuriddinov"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="2%" alt="GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.linkedin.com/in/bektosh-nuriddinov-72b766231/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="2%" alt="LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.youtube.com/@BektoshNuriddinov"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="2%" alt="YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
  <a href="https://www.instagram.com/bektosh_nuriddinov/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-instagram.png" width="2%" alt="Instagram"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="2%">
</div>
