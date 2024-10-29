from datetime import datetime
import secrets
import json
import os

class Edit:
  
  """
  Class for recording or deleting events.
  """
  
  def __init__(self):
    self.datebase  = './datebase.json'
    
  def add(self, title, description, start_time, end_time=None):
    try:
      id = secrets.token_hex(4)
      correct_start = datetime.strptime(start_time, '%Y-%m-%d %H:%M')
      start = correct_start.strftime('%Y-%m-%dT%H:%M')
      if end_time:
        correct_end = datetime.strptime(end_time, '%Y-%m-%d %H:%M') 
        end = correct_end.strftime('%Y-%m-%dT%H:%M')
      else:
        end = end_time
      events = {
        "title": title,
        "description": description,
        "start": start,
        "end": end,
        "id": id 
      }
      if os.path.exists(self.datebase):
        with open(self.datebase, 'r', encoding='utf-8') as filename:
            data = json.load(filename)
            if data == []:
                os.remove(self.datebase)
                return "Restart the function"
      else:
        data = []
      data.append(events)
      with open(self.datebase, 'w', encoding='utf-8') as filename:
        json.dump(data, filename, ensure_ascii=False, indent=2)
        return json.dumps(events, ensure_ascii=False, indent=2)
    except json.JSONDecodeError:
        return "Decoding error json"
    except Exception as e:
        return e

  def delete(self, id):
    try:
      with open(self.datebase, 'r', encoding='utf-8') as file:
        data = json.load(file)
        len_before = (len(data))
        data = [item for item in data if item["id"] != id]
        len_afther = len(data)
        if len_before == len_afther:
          return False
        else: 
          with open(self.datebase, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
            return True
    except FileNotFoundError:
      return 'Calendar not created, use function "add"'
    except json.JSONDecodeError:
      return "Decoding error json"
    except Exception as e:
      return e 