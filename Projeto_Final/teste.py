import os
from PIL import Image
from IPython import display
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pytesseract

def extract_sentences(filename):
  list_break_line = []

  for j in range(1, 6):
    result = pytesseract.image_to_string(
      Image.open(filename + str(j) + '.png'),
      output_type=pytesseract.Output.DICT
    )

    text = result['text']
    line = ''
    for i in range(len(text)):
      if i != len(text)-1:
        if text[i] == '\n' and text[i+1] == '\n':
          list_break_line.append(line)
          line = ''
        elif text[i] == '\n':
          line += ' '
        else:
          line += text[i]

  return list_break_line

def extract_words(filename, verbose=False):
  result = {}

  for j in range(1, 6):
    d = pytesseract.image_to_data(Image.open(filename + str(j) + '.png'), output_type=pytesseract.Output.DICT)
    
    n_boxes = len(d['text'])
    for i in range(n_boxes):
      word = d['text'][i].strip().lower()
      if int(d['conf'][i]) > 60 and len(d['text'][i]) >= 3:
        if word not in list(result.keys()):
          result[word] = d['width'][i]*d['height'][i]
        else:
          result[word] += d['width'][i]*d['height'][i]
        if(verbose):
          display(f"{word} ==> {result[word]}")

  return result

def generate_wordcloud(words_dict, output_filename):
  text_normalized = {}
  text_weights_sum = sum(words_dict.values())
  for k, w in words_dict.items():
    text_normalized[k] = w  / text_weights_sum
  wordcloud = WordCloud(width=4000, height=3000, background_color="white").generate_from_frequencies(text_normalized)
  print(wordcloud)
  plt.figure(figsize=(40,30))
  plt.imshow(wordcloud)
  plt.axis("off")
  plt.savefig(output_filename)
  plt.close()


path_image = os.getcwd() + '/prints/globo'

print(extract_sentences(path_image))

result = extract_words(path_image)

generate_wordcloud(result, 'globo.png')