## Human-Like Typer for Selenium  
This typer writes (and even makes mistakes) like a human. To be used with [Selenium](https://github.com/SeleniumHQ/selenium).  

### Getting Started  
* Install the following packages using pip:  
    ```bash
    pip install selenium
    pip install scipy
    ```
* Download geckodriver from [here](https://github.com/mozilla/geckodriver/releases)  

### Usage  
```python
from utils import setGecko
from typer import Typer

driver = setGecko(executable_path = "/path/to/gecko/executable")
driver.get("https://write-box.appspot.com/")

text = """
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    The quick brown fox jumps over the lazy dog.
    """
element = driver.find_element_by_id('editor')
element.clear()
ty = typer.Typer(accuracy = 0.90, correction_chance = 0.50, typing_delay = (0.04, 0.08), distance = 2)
ty.send(element, text)
```

(https://i.imgur.com/naIJxBC.gif)

**Notes:**  
* **accuracy** determines how often mistakes are made.  
* **correction_chance** determines how often corrections are made.  
* **typing_delay** determines the delay in between each character send.  