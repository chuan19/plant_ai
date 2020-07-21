"# plant_ai" 

train.py --用于训练 注意是用笔记本或台式不是树莓派运行---- tensorflow2.2 python3.8 
代码参考 https://www.tensorflow.org/tutorials/load_data/images?hl=zh_cn
代码参考 https://www.tensorflow.org/tutorials/keras/save_and_load?hl=zh_cn
代码参考 https://www.tensorflow.org/lite/guide/get_started?hl=zh_cn#2_convert_the_model_format


以下用树莓派运行 python3.7 tensoflow1.14
datasets  训练用的数据集
  -photos 里面每个文件夹是不同的类别 预测结果会给出不同类别的概率

tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl 这个是树莓派运行tflite的依赖 用pip3 install ./tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl来安装

predict.py --用于预测
启动示例： python3 predict.py --model ./xxx.tflite(这个是模型)
代码参考：https://www.w3cschool.cn/tensorflow_python/tf_lite_Interpreter.html
代码参考：https://github.com/tensorflow/examples/blob/cf2c52a1ffb98b5f8eb761dcf00346ee3d975b08/lite/examples/object_detection/raspberry_pi/detect_picamera.py#L60

detect.tflite 模型能识别各种东西你可以点开那个labelmap.txt它就是能识别那些玩意
detect_picamera.py 物体识别代码 它依赖annotation.py
启动：
   python3 detect_picamera.py \
  --model ./detect.tflite \
  --labels ./coco_labels.txt