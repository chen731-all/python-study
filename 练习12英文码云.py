import wordcloud as WC
f = open("D:\\文档\\123.txt","r",encoding="gb18030")
txt = f.read()
f.close()
w = WC.WordCloud(width = 1000,height = 700,font_path = "msyh.ttc",background_color = "white")
w.generate(txt)
w.to_file("3.png")