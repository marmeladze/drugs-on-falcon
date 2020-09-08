Steps

0. Navigate somewhere on filesystem and extract files

```bash
$ tar -xvzf src.tar.gz
```


1. Create virtual environment and install dependencies

```bash
$ pwd
/home/ziya/Projects/drugs

$ virtualenv venv && . venv/bin/activate

(venv)$ pip install -r src/requirements.txt
```

2. Navigate to src/api folder and run seeds.py


```bash
$ cd src/api

$ python seeds.py
```

3. Navigate to src folder


```bash
$ cd ../ 
```

Type 


```bash
$ gunicorn --reload api.api
```

Or make run-app.sh executable


```bash
$ chmod +x run-app.sh

$ ./run-app.sh
```
