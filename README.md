# Password Generator

A simple Python-based password generator. Generates secure, random passwords according to length and character-type options.

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation & Usage](#installation--usage)  


---

## Features

- Generate random passwords of a given length.  
- Options to include or exclude:  
  - Uppercase letters  
  - Lowercase letters  
  - Digits  
  - Special symbols  
- Ensures a mix of character types if selected.  
- Easy to run from the command line.  

---

## Prerequisites

- Python 3.6 or newer  
- (Optional) Virtual environment to isolate dependencies  

---

## Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/Bhagvati-Gaikwad/password-generator.git
   cd password-generator
2. (Optional) Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install any dependencies (if applicable). If your script uses only built-in modules, you can skip this.

pip install -r requirements.txt


4. Run the generator:

python3 pg.py


Follow prompts (if your tool asks for password length, type options etc.). The generated password will be printed to the console (or saved/shown as per your implementation).
