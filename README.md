# Convenient Convert
Supported bellow
- Confidence scores of txt files(yolo output) to csv format
- Caf to Wave


# Setup
```
git clone https://github.com/ta-ke-inf/ConvenientConvert.git
cd ConvenientConvert
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
|    -o, --output    |    str   |  ./out  |   Path to output folder or file            |
