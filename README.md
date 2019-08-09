This app counts the lines of python code in a project.

# Requirements

- Python 3
- pygount

# Installation

```
git clone git@github.com:ryanisnan/linecount.git
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Running the App

`python3 main.py /path/to/project`

# Example output

```
matching 	 4449
insights 	 697
career_scales 	 1768
assessments 	 6501
progress 	 565
discoveries 	 1353
location 	 374
member_hijack 	 56
product_emails 	 792
articles 	 263
babelfish 	 151
```

Each directory within your project will show the # of lines of python code contained within.