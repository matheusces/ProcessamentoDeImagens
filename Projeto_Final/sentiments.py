import os
from PIL import Image
from IPython import display
import spacy
from textblob.en import subjectivity
from wordcloud import WordCloud
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
import matplotlib.pyplot as plt
import pytesseract
import pandas as pd


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

def update_dict(dicionario, frase, doc):
  for entidade in doc.ents:
        if entidade.text in dicionario:
          # Atualizando média da polaridade e outros campos 

          newPolarity = dicionario[entidade.text][0] + frase.polarity
          newSubjectivity = dicionario[entidade.text][1] + frase.subjectivity
          newQtd = dicionario[entidade.text][2] + 1

          dicionario[entidade.text] = [
            newPolarity,
            newSubjectivity,
            newQtd,
            newPolarity / newQtd
          ]

        else:
          dicionario[entidade.text] = [
            frase.polarity,
            frase.subjectivity,
            1,
            frase.polarity
          ]

  return dicionario

def detect_sentiment(list_sentences):
  # en_core_web_sm
  # pt_core_news_sm
  # nlp = spacy.load("pt_core_news_sm")
  # nlp.add_pipe('spacytextblob')
  # documento = nlp("This man is bad man!")	

  nlp = spacy.load("pt_core_news_sm")

  dicionario = {}
  # sentiments = []
  for sentence in list_sentences:
    frase = TextBlob(sentence)
    doc = nlp(sentence)

    try: 
      frase_en = TextBlob(str(frase.translate(to='en')))
      dicionario = update_dict(dicionario, frase_en, doc)
    except:
      dicionario = update_dict(dicionario, frase, doc)
      

  return dicionario



path_image_globo = os.getcwd() + '/prints/globo'
path_image_ig = os.getcwd() + '/prints/ig'
path_image_r7 = os.getcwd() + '/prints/r7_'
path_image_terra = os.getcwd() + '/prints/terra_'
path_image_uol = os.getcwd() + '/prints/uol'

globo_sentences = extract_sentences(path_image_globo)
ig_sentences = extract_sentences(path_image_ig)
r7_sentences = extract_sentences(path_image_r7)
terra_sentences = extract_sentences(path_image_terra)
uol_sentences = extract_sentences(path_image_uol)

result = extract_words(path_image_globo)
generate_wordcloud(result, 'globo.png')

result = extract_words(path_image_ig)
generate_wordcloud(result, 'ig.png')

result = extract_words(path_image_r7)
generate_wordcloud(result, 'r7.png')

result = extract_words(path_image_terra)
generate_wordcloud(result, 'terra.png')

result = extract_words(path_image_uol)
generate_wordcloud(result, 'uol.png')

sentiments_globo = detect_sentiment(globo_sentences)
sentiments_ig = detect_sentiment(ig_sentences)
sentiments_r7 = detect_sentiment(r7_sentences)
sentiments_terra = detect_sentiment(terra_sentences)
sentiments_uol = detect_sentiment(uol_sentences)

df = pd.DataFrame(sentiments_globo)
df = df.transpose()
new_df = df.sort_values(by=2)
new_df.tail(25).to_csv("globo_comentarios.csv")

df = pd.DataFrame(sentiments_ig)
df = df.transpose()
new_df = df.sort_values(by=2)
new_df.tail(25).to_csv("ig_comentarios.csv")

df = pd.DataFrame(sentiments_r7)
df = df.transpose()
new_df = df.sort_values(by=2)
new_df.tail(25).to_csv("r7_comentarios.csv")

df = pd.DataFrame(sentiments_terra)
df = df.transpose()
new_df = df.sort_values(by=2)
new_df.tail(25).to_csv("terra_comentarios.csv")

df = pd.DataFrame(sentiments_uol)
df = df.transpose()
new_df = df.sort_values(by=2)
new_df.tail(25).to_csv("uol_comentarios.csv")