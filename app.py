
from flask import Flask, render_template , request
from PIL import Image
import cv2
from yolo_detection_images import runModel
import cap

#__name__=__main__
app=Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def predict():
	if request.method=='POST':
		f=request.files['userfile']
		path="./static/{}".format(f.filename)
		f.save(path)

		#caption generation
		caption = cap.generate_caption(path)

		#object detection
		img = cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)
		img = runModel(img)
		img = Image.fromarray(img.astype("uint8"))
		location="./static/obj{}".format(f.filename)
		img.save(location)

		#dictionary with results
		result={
		'image': path,
		'obj':location,
		'caption': caption
		}
		print(caption)

	return render_template("output.html", output=result)

if __name__=="__main__":
	app.run(debug=True)