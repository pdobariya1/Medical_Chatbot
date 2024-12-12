# Medical_Chatbot_using_Llama

### Use the Llama 3.1 Model from Nvidia

https://build.nvidia.com/meta/llama-3_1-8b-instruct 

## Steps to run the project

### 1. Create Virtual Environment
```bash
conda create -p mvenv python=3.9 -y
```

### 2. Activate Environment
```bash
conda activate ./mvenv
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Create Index
- For Windows
```bash
python store_index.py
```
- For Linux
```bash
python3 store_index.py
```

### 5. If you have already index, run following command
- For Windows
```bash
python app.py
```
- For Linux
```bash
python3 app.py
```