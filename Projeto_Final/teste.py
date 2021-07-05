import os
from PIL import Image
from IPython import display
from textblob.en import subjectivity
from wordcloud import WordCloud
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
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

def obter_dados_das_fontes():
    diretorio_base = os.getcwd()

    with open(diretorio_base + "training/imdb_labelled.txt", "r") as arquivo_texto:
        dados = arquivo_texto.read().split('\n')
         
    with open(diretorio_base + "training/amazon_cells_labelled.txt", "r") as arquivo_texto:
        dados += arquivo_texto.read().split('\n')

    with open(diretorio_base + "training/yelp_labelled.txt", "r") as arquivo_texto:
        dados += arquivo_texto.read().split('\n')

    return dados

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

  # print(documento.text)
  # for token in documento:
  #   print(token.text, token.pos_, token.dep_)

  # print('\n')
  # documento = nlp('Bill Gates nasceu em Seattle em 28/10/1955 e foi criador da Microsoft')
  # for entidade in documento.ents:
  #   print(entidade.text, entidade.label_)
  
  # documento = nlp("Este homem é realmente mau!")	
  # print(
  #   documento._.polarity,
  #   documento._.subjectivity,
  #   documento._.assessments
  # )
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

    print(dicionario)
      

  return dicionario

  # print(frase_en.tags)
  # print("Polaridade: ", frase_en.polarity) # -1 < p < 1
  # print("Subjetividade: ", frase_en.subjectivity) # 0 < p < 1
  # print('\n', frase_en.sentiment_assessments)




path_image = os.getcwd() + '/prints/globo'

globo_sentences = extract_sentences(path_image)

# #result = extract_words(path_image)

# #generate_wordcloud(result, 'globo.png')

sentiments = detect_sentiment(globo_sentences)
print(sentiments)

# text = TextBlob("Que dia tão ruim de bom")
# text = text.translate(to="en")
# print(text)
# nlp = spacy.load("pt_core_news_sm")
# doc = nlp('Que dia tão ruim de bom')
# for ent in doc.ents:
#   print(ent.text)
# print(text.sentiment_assessments)