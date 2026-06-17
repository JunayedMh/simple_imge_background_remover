# Simple Image Background Remover

A beginner-friendly Python script that removes the background from any image using the `rembg` library. Just run the script, paste your image path, and get a clean transparent PNG — no complicated setup needed!

---

## Features

- Removes background from any image automatically
- Saves output as PNG with transparent background
- Automatically names the output file (adds `_no_bg` to original name)
- Handles Windows file paths with quotes and backslashes
- Loop mode — remove multiple images in one session without restarting

---

## Requirements

- Python 3.7+
- rembg
- Pillow

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/JunayedMh/simple_imge_background_remover.git
cd simple_imge_background_remover
```

**2. Install dependencies**
```bash
pip install "rembg[cpu]" Pillow
```

> If you have an NVIDIA GPU, use `pip install "rembg[gpu]"` for faster processing.

---

## Usage

**Run the script:**
```bash
python removebg.py
```

**Then follow the prompt:**
```
--- Background Remover ---

Enter your image path here: G:\Photos\photo.jpg
Reading path as: G:\Photos\photo.jpg

Opening image...
Removing background... (this may take a few seconds)
✅ Done! Saved as: G:\Photos\photo_no_bg.png

Do you want to remove another background? (y/n):
```

---

## How to Copy Image Path on Windows

1. Go to your image file
2. Hold `Shift` + Right click
3. Click **"Copy as path"**
4. Paste it into the terminal — the script handles the quotes automatically!

---

## Output

The output file is saved in the **same folder** as your original image with `_no_bg` added to the filename.

| Input | Output |
|---|---|
| `photo.jpg` | `photo_no_bg.png` |
| `portrait.png` | `portrait_no_bg.png` |
| `image.webp` | `image_no_bg.png` |

---

## Common Issues

**`No onnxruntime backend found` error:**
```bash
pip install "rembg[cpu]"
```

**File not found error:**
- Make sure you paste the full path
- The script automatically removes quotes, so no need to delete them manually
- Try using forward slashes `/` instead of backslashes `\` if issues persist

---

## 📄 License

MIT License — feel free to use and modify!