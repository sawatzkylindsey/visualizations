# visualizations


### Setup

    # Virtual Environment
    python3 -m venv p3
    source p3/bin/activate

    # Libraries (pypi)
    pip install dateutils
    
    # Libraries (custom)
    curl -LO https://github.com/sawatzkylindsey/pytils/archive/master.zip
    cd pytils-master/
    python setup.py install
    
    curl -LO https://github.com/sawatzkylindsey/otter/archive/master.zip
    cd otter-master/
    python setup.py install


### Run

    python serve.py -h

    python serve.py timeline_file.json
    # the open: http://localhost:8888/index.html

