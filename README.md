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
|    --train_size    |    float  |  0.7   |   train data rate                          |
|    --test_size     |    float  |  0.3   |   test data rate                           |
|    --shuffle       |    bool   |  True  |   Are you shuffle dataset?                 |
|    --random_state  |    int    |  0     |   What is randam seed?                     |
|    --stratify      |    bool   |  True  |   Are you stratify each labels?            |
