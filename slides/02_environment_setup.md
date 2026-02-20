---
marp: true
paginate: true
theme: default
---

<!-- markdownlint-disable-file MD029 MD036 MD026 -->

# Environment Setup

## Getting Ready for Development

---

## Prerequisites (1/2)

- **Python 3.10+**: Ensure Python is installed.
  - Check with `python --version`
- **MongoDB Atlas Account**:
  - Free tier works perfectly.
  - Sign up at `mongodb.com/atlas`.

---

## Prerequisites (2/2)

- **VoyageAI API Key**:
  - Sign up at `voyageai.com`.
  - Create a new API Key.
  - Save it safely! (We'll use it soon).

---

## Step 1: Python Virtual Environment (1/3)

- Why use a virtual environment?
  - Isolates dependencies.
  - Prevents conflicts with system Python.
  - Keeps project clean.

---

## Step 1: Python Virtual Environment (2/3)

- **Create with uv**:

```bash
uv venv
```

- **Activate (Mac/Linux)**:

```bash
source .venv/bin/activate
```

- **Activate (Windows)**:

```bash
.venv\Scripts\activate
```

---

## Step 1: Python Virtual Environment (3/3)

- You should see `(.venv)` in your terminal prompt.
- `uv` is much faster than standard `venv`.

---

## Step 2: Installing Dependencies (1/4)

- We need several libraries.
- Create a `requirements.txt` file (optional, or install directly).

---

## Step 2: Installing Dependencies (2/4)

- **Core Libraries**:

```bash
uv pip install django pymongo
```

- **AI & Search Libraries**:

```bash
uv pip install langchain langchain-community voyageai
```

---

## Step 2: Installing Dependencies (3/4)

- **Visualization & Utilities**:

```bash
uv pip install gradio python-dotenv
```

- **Note**: `uv` installs packages in parallel, making it very fast.

---

## Step 2: Installing Dependencies (4/4)

- Verify installation:

```bash
uv pip list
```

- Check for meaningful output (lists installed packages).

---

## Step 3: Setting Up MongoDB Atlas (1/5)

- **Create a Cluster**:
  - Login to Atlas.
  - Click **+ Create**.
  - Select **M0 Sandbox** (Free Tier).
  - Choose a region close to you (e.g., Singapore/Tokyo for Asia).
  - Click **Create Deployment**.

---

## Step 3: Setting Up MongoDB Atlas (2/5)

- **Create Database User**:
  - Security -> Database Access.
  - Add New Database User.
  - Method: **Password**.
  - Username: `workshop_user`.
  - Password: `workshop_password` (Make it strong!).
  - Built-in privileges: **readWriteAnyDatabase**.

---

## Step 3: Setting Up MongoDB Atlas (3/5)

- **Network Access**:
  - Security -> Network Access.
  - Add IP Address.
  - Allow Access from Anywhere (`0.0.0.0/0`) for this workshop.
  - **Note**: In production, whitelist only your App Server IP!

---

## Step 3: Setting Up MongoDB Atlas (4/5)

- **Get Connection String**:
  - Click **Connect** on your cluster.
  - Drivers -> Python -> Version 3.6 or later.
  - Copy the connection string!
  - Format: `mongodb+srv://<username>:<password>@cluster0.xyz.mongodb.net/?retryWrites=true&w=majority`

---

## Step 3: Setting Up MongoDB Atlas (5/5)

- **Replace placeholders**:
  - Replace `<username>` with `workshop_user`.
  - Replace `<password>` with your actual password.

---

## Step 4: Testing the Connection (1/3)

- Create a file `test_mongo.py`.
- Import `pymongo`.

```python
from pymongo import MongoClient
import os

# Ideally load from env
uri = "your-connection-string" 

client = MongoClient(uri)
```

---

## Step 4: Testing the Connection (2/3)

- Send a Ping to confirm connection.

```python
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
```

---

## Step 4: Testing the Connection (3/3)

- Run the script:

```bash
python test_mongo.py
```

- Success? Move on!
- Failure? Check IP Whitelist and Password.

---

## Step 5: Configuring VoyageAI (1/3)

- Make sure you copied your API Key.
- Best practice: Use `.env` file.

---

## Step 5: Configuring VoyageAI (2/3)

- Create `.env` file in project root:

```env
VOYAGE_API_KEY=vy-your-key-here
MONGO_URI=mongodb+srv://...
```

---

## Step 5: Configuring VoyageAI (3/3)

- Test VoyageAI connection:

```python
import voyageai
import os
from dotenv import load_dotenv

load_dotenv()

client = voyageai.Client(api_key=os.getenv("VOYAGE_API_KEY"))
result = client.embed(["Hello, world!"], model="voyage-large-2")
print(result.embeddings[0][:5]) # Print first 5 dimensions
```

---

## Environment Check Complete

- Python Installed ✅
- Virtual Env Active ✅
- Libraries Installed ✅
- MongoDB Connected ✅
- VoyageAI Key Active ✅
- **Ready for Chunking!**
