# Best practice to call load_dotenv():

✅ call load_dotenv() once at the application entry point
NOT inside every class/module.

# Production-Grade Pattern

```Python
main.py
from dotenv import load_dotenv

load_dotenv()

def main():
...

if **name** == "**main**":
main()
```

# Even Better (Large Apps)

Create dedicated config module:

config.py

```python
from dotenv import load_dotenv
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

Then:

```python
from app.config import OPENAI_API_KEY
```

# Useful for:

FastAPI
Django
enterprise apps
multi-env deployments
