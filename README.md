# EdgeFarm

This script automates Microsoft Rewards searches in your browser.

> **FOR EDUCATIONAL PURPOSES ONLY. USE AT YOUR OWN RISK.**

## How It Works

The script triggers a hotkey (Ctrl + E for Edge), which opens a search pop-up. It then generates four random letters followed by a number indicating the remaining iterations (searches). Example: `hsow18` — "h", "s", "o", and "w" are the random letters, and 18 searches are left.

Searches are performed approximately every 10 seconds.

## How to Use

### 1. Install Python

Download and install the latest **stable** version of Python from:
- [Official Website](https://www.python.org/downloads/)
- [Microsoft Store](https://apps.microsoft.com/detail/9nrwmjp3717k?hl=en-us&gl=US)

### 2. Install the Program

Clone the repository using:
```sh
git clone https://github.com/evolvedoff/edgefarm.git
```
To open CMD in a specific folder, navigate to it in File Explorer and type **"cmd"** in the path bar.

Alternatively, download the latest release from [here](https://github.com/evolvedoff/edgefarm/releases) and extract it to a folder of your choice.

### 3. Install Required Libraries

Open CMD in the project folder and run:
```sh
pip install -r requirements.txt
```
If you encounter issues with `pip`, update it first:
```sh
python -m ensurepip --default-pip
python -m pip install --upgrade pip
```
Or install the required libraries manually:
```sh
pip install pyautogui keyboard wonderwords
```

### 4. Run the Program

Navigate to the project folder in CMD and run:
```sh
python main.py
```
**Ensure you are in the correct folder** before running `main.py` to avoid executing unintended files.

### 5. Using the Program

Once the CMD window opens, switch to your browser and press **F1**. The script will begin searching automatically.

#### Stopping the Program
- Hold **F1** until a new tab opens—this indicates the program has stopped.
- If this does not work, wait for it to finish (it runs for 5 minutes) or close the CMD window manually.

> **Note:** Pausing the script with F1 can be inconsistent. If needed, restart it later.

## License

This project is licensed under **GPL-3.0**. You are free to use, modify, and distribute it as long as you comply with GPL-3.0. While credit is not required, it is appreciated.

## Credits

Expecting someone else? Nope, just me! 😉

By the way, check out my YouTube channel: [@evolveroff](https://www.youtube.com/@evolveroff)!

> **Note:** Middle-click the link to open it in a new tab.

## Legal Disclaimer

This software is provided **for educational purposes only**. The author is not responsible for any misuse. Users are solely responsible for ensuring compliance with applicable laws and platform terms, including Microsoft Rewards policies.

By using this script, you accept all risks. **Use at your own discretion.**
