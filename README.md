# simple_imge_background_remover

A simple Python script that removes the background from an image using the `rembg` library.

## Features

- Removes image backgrounds automatically
- Saves output as a PNG with transparent background
- Works with common image formats

## Requirements

- Python 3.8+
- `rembg`
- `Pillow`

## Installation

1. Create or activate a Python virtual environment (recommended):

```powershell
python -m venv venv
.\
env\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install rembg Pillow
```

> If you want the CPU-only version of `rembg`, install it with:
>
> ```powershell
> pip install "rembg[cpu]"
> ```

## Usage

Run the script and enter the image file path when prompted:

```powershell
python removebg.py
```

Example input:

```text
Enter your image path here: C:\path\to\image.jpg
```

The script will create a new file next to the original image with the suffix `no_background.png`.

## Run in VS Code (local)

1. Open the folder in VS Code.
2. Open a new terminal in VS Code (`Terminal > New Terminal`).
3. Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies if not already installed:

```powershell
pip install rembg Pillow
```

5. Run the script in the terminal:

```powershell
python removebg.py
```

6. Enter the image path when prompted.

## Run in GitHub Codespaces

1. Open the repository in a GitHub Codespace.
2. Open the integrated terminal.
3. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install rembg Pillow
```

5. Run the script:

```bash
python removebg.py
```

6. Provide the image path in the prompt.

## Output

If the input is `photo.jpg`, the output will be:

- `photo no_background.png`

## Notes

- Make sure the image path is correct.
- The script supports transparent background output only in PNG format.
