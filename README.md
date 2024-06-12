# The Boring Academy Key Store Manager

Welcome to the Boring Academy Key Store Manager! This application allows you to manage activation keys for courses offered by The Boring Academy. Below you will find a comprehensive guide on how to set up, run, and use this application effectively.

## Table of Contents
* [Features](#Features)
* [Installation](#Installation)
* [Configuration](#Configuration)
* [Contributing](#Contributing)
* [License](#License)


## Features
* Manage Activation Keys: Generate unique activation keys for courses offered by The Boring Academy.
* Manage Subjects and Courses: Add and regroup subjects and courses offered by The Boring Academy.
* Generate Analytics Report: Generate a report to determine revenue and key factors to enhance commercialization.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/softsurgery/the-boring-academy-key-store-manager.git
cd the-boring-academy-key-store-manager
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate
```

3.Install the required packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up Firebase:
* Create a Firebase project.
* Generate a service account key and download the JSON file.
* Save the JSON file in your project directory and update the firebase_admin initialization code with the path to your JSON file.

2. Initialize Firebase in your code:

```python
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/your/firebase/credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-database-name.firebaseio.com'
})
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.



