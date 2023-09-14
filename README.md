<div align="center">
  <img src="https://raw.githubusercontent.com/Ikomia-hub/dataset_yolo/main/icons/yolo.png" alt="Algorithm icon">
  <h1 align="center">dataset_yolo</h1>
</div>
<br />
<p align="center">
    <a href="https://github.com/Ikomia-hub/dataset_yolo">
        <img alt="Stars" src="https://img.shields.io/github/stars/Ikomia-hub/dataset_yolo">
    </a>
    <a href="https://app.ikomia.ai/hub/">
        <img alt="Website" src="https://img.shields.io/website/http/app.ikomia.ai/en.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/Ikomia-hub/dataset_yolo/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/Ikomia-hub/dataset_yolo.svg?color=blue">
    </a>    
    <br>
    <a href="https://discord.com/invite/82Tnw9UGGc">
        <img alt="Discord community" src="https://img.shields.io/badge/Discord-white?style=social&logo=discord">
    </a> 
</p>

Load YOLO dataset. This plugin converts a given dataset in YOLO format to Ikomia format. Once loaded, all images can be visualized with their respective annotations. Then, any training algorithms from the Ikomia marketplace can be connected to this converter.

![Example](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3400968%2Fbcdae0b57021d6ac3e86a9aa2e8c4b08%2Fts_detections.gif?generation=1581700736851192&alt=media)

## :rocket: Use with Ikomia API

#### 1. Install Ikomia API

We strongly recommend using a virtual environment. If you're not sure where to start, we offer a tutorial [here](https://www.ikomia.ai/blog/a-step-by-step-guide-to-creating-virtual-environments-in-python).

```sh
pip install ikomia
```

#### 2. Create your workflow


```python
from ikomia.dataprocess.workflow import Workflow

# Init your workflow
wf = Workflow()

# Add dataset loader
dataset = wf.add_task(name="dataset_yolo", auto_connect=False)

# Set parameters
dataset.set_parameters({'dataset_folder': 'path/to/images/and/annotations',
                        'class_file': 'path/to/classes.names'})

# Add training algorithm for object detection
train_algo = wf.add_task(name="train_yolo_v8", auto_connect=True)

# Run whole workflow
wf.run()
```

Example of YOLO dataset : [traffic signs](https://www.kaggle.com/datasets/valentynsichkar/traffic-signs-dataset-in-yolo-format?resource=download).

## :sunny: Use with Ikomia Studio

Ikomia Studio offers a friendly UI with the same features as the API.

- If you haven't started using Ikomia Studio yet, download and install it from [this page](https://www.ikomia.ai/studio).

- For additional guidance on getting started with Ikomia Studio, check out [this blog post](https://www.ikomia.ai/blog/how-to-get-started-with-ikomia-studio).

## :pencil: Set algorithm parameters

- **dataset_folder** (str): Path to the dataset folder.
- **class_file** (str): Path to text file containing class names.

*Note*: parameter key and value should be in **string format** when added to the dictionary.
## :mag: Explore algorithm outputs

Every algorithm produces specific outputs, yet they can be explored them the same way using the Ikomia API. For a more in-depth understanding of managing algorithm outputs, please refer to the [documentation](https://ikomia-dev.github.io/python-api-documentation/advanced_guide/IO_management.html).

```python
import ikomia
from ikomia.dataprocess.workflow import Workflow

# Init your workflow
wf = Workflow()

# Add algorithm
algo = wf.add_task(name="dataset_yolo", auto_connect=True)

# Run on your image  
wf.run_on(url="example_image.png")

# Iterate over outputs
for output in algo.get_outputs():
    # Print information
    print(output)
    # Export it to JSON
    output.to_json()
```

