import time
import discord
import pytz
import datetime
from replit import db
from functions.rym import *
from functions.discogs import *
from functions.helpers import *
from functions.user import *


def add_new_show(message):  
  new_show = message.split(' - ')
  show = new_show[1]
  artists = new_show[2]
  date = new_show[3]
  url = new_show[4]      
    
  item = {
      'show': show,
      'artists': artists,
      'date': date,
      'url': url
  }  
  db['shows'].append(item)
  print('new: ',item)
  embedVar = discord.Embed(
    title=f'Show {item["show"]} inserido com sucesso!', color=0x00ff00
  )
  embedVar.add_field(
                    name='\u200b',
                    value= item['show'],
                    inline=False
            ) 
  print(type(item))
  

  return embedVar


def get_shows():
  unsorted_list = []
  today = datetime.date.today()
  for item in db['shows']:
    new = item    
    show_date = datetime.datetime.strptime(new['date'].replace('/', ''), "%d%m%Y").date()
    remaining_days = show_date - today
    new['remaining_days'] = remaining_days.days    
    unsorted_list.append(new)
  
  sorted_list = sorted(unsorted_list, key=lambda d: d['remaining_days'], reverse=False) # Atenção ao reverse para definir a ordem
  for item in unsorted_list:
    print(item['remaining_days'])

  embedVar = discord.Embed(title='Próximos Shows', color=0x0093FF)        

  text = ''
  for item in sorted_list:
      date = item['date'][0:5]
      show = item['show']
      artists = item['artists']
      remaining = item['remaining_days']
      text += f'{date} - **[{show}]({item["url"]})** - daqui a **{remaining} dias**\n'
  text += '\n\u200b'
  try:
      embedVar.add_field(
      name='\u200b',
      value= text
        ) 
  except:
      print('deu algum erro')
  embedVar.set_footer(text='Clique no show para acessar o site do evento.')
  return embedVar

