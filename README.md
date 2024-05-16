# TicTacTo
TicTacTo is a little Project written in Python. It is a TicTacTo game **purely** in the console. It is just using **one external library** which is [keyboard](https://pypi.org/project/keyboard/).

It's not that simple there is a *little surprise*. You can play against an ***AI (based on [minimax](https://en.wikipedia.org/wiki/Minimax) algorithm)*** or you can just play locally with a friend.

## Reward
The **_first two people_** who can **_beat the AI without changing the source code_** can win **_10$_**.
Good luck!

## Installation
The Project is build in Python version 3.12.
After you downloaded or cloned the Repo, go into TicTacTo (if you download as zip it's TicTacTo - master) directory.
It is recommended to create a virtual environment like this:

```bash
python -m venv .venv
```

<hr>

Then activate the virtual environment.

- On Linux/MacOs:
```bash
source .venv/bin/activate
```

- On Windows:
```bash
.venv\Scripts\activate.bat
```

<hr>

In the venv now use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

Now change directory to source folder and run:
```bash
cd source
```
```bash
python run.py
```

<hr>

After playing deactivate the venv like this:
```bash
deactivate
```

## Controls
1. **WASD** to move the cursor
2. **Enter** to confirm the current field and flip turns.

## Preview
![image](https://github.com/mert-eryl14/YoutubeDownloader-GUI/assets/85054971/2eec6e27-cd68-4dab-b0fa-aac9ce3ca183)

<hr>

![image](https://github.com/mert-eryl14/YoutubeDownloader-GUI/assets/85054971/70c467a9-2fcc-4f0b-8f42-0b827105e744)

<hr>

![image](https://github.com/mert-eryl14/YoutubeDownloader-GUI/assets/85054971/6c7ec521-e5cf-4414-8a2c-4f15827ba0f0)

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.