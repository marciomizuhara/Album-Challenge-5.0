import discord
from replit import db
from functions.helpers import *


def myratings_list(user, year):
  unsorted_list = []  
  list1 = [x for x in db['2022']]
  list2 = [x for x in db['2023']]
  iterable_list = list1 + list2  
  for item in iterable_list:
    for nota in item['rating']:                        
        if nota == user:                            
                     
            new_entry = {
                'id': item['id'],
                'artist': item['artist'],
                'album': item['album'],
                'rating': item['rating'][nota],
                'year': item['year'],
                'cover': item['cover'],
                'spotify': item['spotify'],
            }
            unsorted_list.append(new_entry)            
  if year == 'alltime':
    sorted_list = sorted(unsorted_list, key=lambda d: d['rating'], reverse=True)    
    return sorted_list[0:20]
  else:
    year_list = [x for x in unsorted_list if x['year'] == year]
    sorted_list = sorted(year_list, key=lambda d: d['rating'], reverse=True)    
    return sorted_list


def getratings(lista, album_id):
  pass


def update_album_rating(user, id, rating):    
    lista = list_helper(id)
    id = id_helper(id)    
    if str(user) in db.keys():
        if str(user) not in db[lista][id]['rating'].keys():
          db[lista][id]['rating'][str(user)] = {}
        db[lista][id]['rating'][str(user)] = rating
    else:
        pass

def get_rating_average(id):
    album_id = id_helper(id)
    average = []
    lista = list_helper(id)        
    try:
      for rating in db[lista][album_id]['rating'].items():
        user_rating = rating[1]
        average.append(user_rating)
      album_rating = str(sum(average) / len(average))[:3]
      return album_rating
    except:
      return 'Ainda sem notas'


def myratings_embeds(sorted_list, user, year):
  # for item in sorted_list:
  #   print(item['artist'])
  counter = 1                
  embedSet = []
  embedVar = discord.Embed(
    title=f'Melhores avaliados por {user} ({year})', color=0x0093FF
  )
  text = ''        
  embedVar.set_thumbnail(
        url = sorted_list[0]['cover']
      )
  for item in sorted_list[0:7]:
      try:
        album = item["artist"] + ' - ' + item["album"]
        if len(album) > 36:
          album = album[0:36] + '...'  
        if counter == 1:
          counter = '👑'
          text += f'**{counter}. [{album} ({item["year"]})]({item["spotify"]})** - nota: **{item["rating"]}**\n'                
          counter = 1
          counter += 1              
        else:
          text += f'**{counter}. [{album} ({item["year"]})]({item["spotify"]})** - nota: **{item["rating"]}**\n'
          counter += 1                
        # if counter > 7:
        #     break
      except:
        continue
  try:
    embedVar.add_field(
    name='\u200b',
    value= text
      )
    embedSet.append(embedVar)
  except:
      pass
  
  if len(sorted_list) > 7:
    embedVar2 = discord.Embed(color=0x0093FF)
    text2 = ''
    for item in sorted_list[7:14]:
      try:
        album = item["artist"] + ' - ' + item["album"]
        if len(album) > 36:
          album = album[0:36] + '...'       
        text2 += f'**{counter}. [{album} ({item["year"]})]({item["spotify"]})** - nota: **{item["rating"]}**\n'
        counter += 1                
        # if counter > 7:
        #     break
      except:
        continue
  try:
    embedVar2.add_field(
    name='\u200b',
    value= text2
      )
    embedSet.append(embedVar2)
  except:
      pass

  if len(sorted_list) > 14:
    embedVar3 = discord.Embed(color=0x0093FF)
    text3 = ''
    for item in sorted_list[14:20]:        
        try:
          album = item["artist"] + ' - ' + item["album"]
          if len(album) > 36:
            album = album[0:36] + '...'          
          text3 += f'**{counter}. [{album} ({item["year"]})]({item["spotify"]})** - nota: **{item["rating"]}**\n'
          counter += 1                
          # if counter > 7:
          #     break
        except:
          continue
    try:
      embedVar3.add_field(
      name='\u200b',
      value= text3
        )
      embedSet.append(embedVar3)
    except:
        pass

  return embedSet
  
  