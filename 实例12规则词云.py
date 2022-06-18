import jieba as J
import wordcloud as WC
f = open("D:\\文档\\庆余年.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = J.lcut(t)
txt = "".join(ls)
w = WC.WordCloud(font_path = "msyh.ttc",width = 1000,height = 700,background_color = "white")
w.generate(txt)
w.to_file("gr.png")
