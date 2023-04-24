# Convenient Convert
Supported bellow
- Confidence scores of txt files(yolo output) to csv format
- Caf to Wave


# Setup
```
git clone https://github.com/ta-ke-inf/conf-txt2csv.git
cd conf-txt2csv
pip install -r requirements.txt
```
# Run
```
python yolo_txt2csv.py -i ./in -o ./out/output.csv
            caf2wav.py            ./out
```

|  option  |  type  |  default  |  description  |
|  ------  |  ----  |  -------  |  -----------  |
|    -i, --input    |    str   |  ./in  |   Path to input folder or file            |
|    -o, --output    |    str   |  ./out/output.csv  |   Path to output folder or file            |
