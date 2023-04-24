# conf-txt2csv
Confidence scores of txt files to csv format


# Setup
```
git clone https://github.com/ta-ke-inf/conf-txt2csv.git
cd conf-txt2csv
pip install -r requirements.txt
```
# Run
```
python main.py -i ./in -o ./out/output.csv
```

|  option  |  type  |  default  |  description  |
|  ------  |  ----  |  -------  |  -----------  |
|    -i, --input    |    str   |  ./in  |   Path of the folder where the txt file output from yolo resides            |
|    -o, --output    |    str   |  ./out/output.csv  |   Path where the csv file to be written exists            |
