from datetime import datetime
import json
import os

class Check:
  
  """
  Class for viewing events with different conditions.
  """
  
  def __init__(self):
    self.datebase  = './datebase.json'
    
  def today(self):
    try:
      now = datetime.now()
      today = now.strftime('%Y-%m-%d')
      with open(self.datebase, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_new = []
      
        for item in data:
          start_time = item["start"]
          end_time = item["end"]
          datetime_start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        
          if end_time:
            datetime_end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')
            end_only = datetime_end.strftime('%Y-%m-%d')
          else:
            pass
          start_only = datetime_start.strftime('%Y-%m-%d')
          if today == start_only or today == end_only:
            data_new.append(item)
          else:
            pass
          if data_new:
            return json.dumps(data_new, ensure_ascii=False, indent=4)
          else:
            return False
    except FileNotFoundError:
      return 'Calendar not created, use function "add"'
      
    except json.JSONDecodeError:
      return "Decoding error json"
      
    except Exception as e:
      return e

  def now(self):
    try:
      now_date = datetime.now()
      now = now_date.strftime('%Y-%m-%d %H:%M')
      with open(self.datebase, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_new = []
      
        for item in data:
          start_time = item["start"]
          end_time = item["end"]
          datetime_start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
          datetime_end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M') if end_time else now_date
        
          if datetime_start <= now_date <= datetime_end:
            data_new.append(item)
          
      return json.dumps(data_new, ensure_ascii=False, indent=4)
    except FileNotFoundError:
      return 'Calendar not created, use function "add"'
    except json.JSONDecodeError:
      return "Decoding error json"
    except Exception as e:
      return e

  def archive(self):
    try:
      now_date = datetime.now()
      now = now_date.strftime('%Y-%m-%d %H:%M')
      with open(self.datebase, 'r', encoding='utf-8') as file:
        data = json.load(file)
        data_new = []
      
        for item in data:
          start_time = item["start"]
          end_time = item["end"]
          datetime_start = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
          datetime_end = datetime.strptime(end_time, '%Y-%m-%dT%H:%M') if end_time else now_date
        
          if datetime_start <= now_date and datetime_end <= now_date:
            data_new.append(item)
          
        return json.dumps(data_new, ensure_ascii=False, indent=4)
    except FileNotFoundError:
      return 'Calendar not created, use function "add"'
    except json.JSONDecodeError:
      return "Decoding error json"
    except Exception as e:
      return e

  def history(self):
    try:
      with open(self.datebase, 'r', encoding='utf-8') as calend:
        data = json.load(calend)
        if not data:
          return "Empty"
        else:
          return json.dumps(data, ensure_ascii=False, indent=4)
    except FileNotFoundError:
      return 'Calendar not created, use function "add'
    except json.JSONDecodeError:
      return "Decoding error json"
    except Exception as e:
      return e