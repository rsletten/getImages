## Getting Started
### Prerequisites
- Python 3. I'm using Python 3.8.6
- [chromedriver](https://chromedriver.chromium.org/downloads) in your path
- virtualenv
- requests
- selenium
- imageio

### Basic Installation

```shell
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
mkdir screenshots
```

### Usage

#### Make sure you are within the virtualenv

```shell
source venv/bin/activate
```

#### Getting the images
```shell
python3 getImage.py 0 30
```
0: start today
30: collect 30 days of images previous to today

#### Creating the animation

images are stored in the screenshots folder

```shell
python3 createGif.py
```
