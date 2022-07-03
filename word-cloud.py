from wordcloud import WorldCloud,STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"file.csv")
comment=''
stopwords=set(STOPWORDS)

for val in df.CONTENT:
    val=str(val)
    tokens=val.split()
    for i in range(len(tokens)):
        tokens[i]=tokens[i].lower()
    comment+=" ".join(tokens)+" "
worldcloud=WorldCloud(width=800,height=800,background_color='white',
stopwords=stopwords,min_font_size=10).generate(comment)

plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(worldcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()