from roboflow import Roboflow
rf = Roboflow(api_key="GWPLfbanlFRrU2iDQm6w")
project = rf.workspace("rostselmash").project("rostselmash")
version = project.version(1)
dataset = version.download("yolov8")