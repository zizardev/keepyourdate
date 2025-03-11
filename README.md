# KeepYourDate

## What is this? 
This is a **simple** library for storing and viewing events.

## Quick Guide 
```python
from keepyourdate import *
add("Name event", "Description event", "start date (example: 2024-10-28 10:00)", "end date(example: 2024-10-30 20:00)")
history()
```
Great job adding your first event. 

---

### Using
Delete event (To find out the ID use the command: `history`. 
```python
delete(id)
```
Reading events in different ways
```python
history() #All events.
today() #Events for today.
now() #Events that are happening at this hour.
archive() #Events that have expired.
```
---
## Developer 
my website: [click](https://zizardev.github.io/website/index.html]
pypi: [click](https://pypi.org/project/keepyourdate/)
