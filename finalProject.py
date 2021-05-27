from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import csv
import os

import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('FrontPage.html')

@app.route('/hi',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
        result = request.form["name"]
        
        
        l = list(result)
        l[len(l)-1] = "{}"
        inp = ''.join(map(str, l))#converting last character to {}
        print(inp)


        pages = [1,2,3]
        with open('E:\ScrapData\Scrap.txt', 'w', encoding='utf-8', newline='') as f_output:
            csv_print = csv.writer(f_output)
            emptyfile = os.stat('E:\ScrapData\Scrap.txt').st_size == 0
            if emptyfile:
                csv_print.writerow(['Reviews'])
            for page in pages:
                source = requests.get(inp.format(page)).text
                soup = BeautifulSoup(source, 'lxml')

                for ren in soup.find_all('div',class_='a-row a-spacing-small review-data'):
                    try:
                        review = ren.span.text
                    except Exception as e:
                        review = None
                    csv_print.writerow([review])
                    
                    
            
                    



        
        f = open("E:\ScrapData\Scrap.txt", "r+", encoding="utf8")
        sentence = f.read()
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(sentence)
        print("Overall sentiment dictionary is : ", sentiment_dict) 
        print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
        print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
        print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
      
        print("Sentence Overall Rated As", end = " ") 
      
        # decide sentiment as positive, negative and neutral 
        if sentiment_dict['compound'] >= 0.05 :
            print("Positive") 
      
        elif sentiment_dict['compound'] <= - 0.05 : 
            print("Negative") 
      
        else : 
            print("Neutral")




     #GRAPH



        x = ["Negative","Neutal","Positive"]
        a = sentiment_dict['neg']*100
        b = sentiment_dict['neu']*100
        c = sentiment_dict['pos']*100
        y=[a,b,c]
        barlist = plt.bar(x,y,label ='Rating')
        barlist[0].set_color('r')
        barlist[1].set_color('g')
        barlist[2].set_color('y')
        plt.ylim(0,100) 
         

        plt.xlabel('Sentiments')
        plt.ylabel('Percentage')
        plt.title('Overall Rating')
        plt.legend()
        strFile = "C:\\Users\Shaikh\BE PROJECT\static\p1.png"
        if os.path.isfile(strFile):
           os.remove(strFile)   # Opt.: os.system("rm "+strFile)
        plt.savefig(strFile)
        plt.show()

        

    #Graph2
        labels = "Negative","Neutal","Positive"
        sizes = [a,b,c]
        explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        strFile = "C:\\Users\Shaikh\BE PROJECT\static\p2.png"
        if os.path.isfile(strFile):
           os.remove(strFile)   # Opt.: os.system("rm "+strFile)
        plt.savefig(strFile)
        plt.show()
       

    #Graph3

        x = ["NEGATIVE","NEUTRAL","POSITIVE"]
        y = [a,b,c]
        plt.scatter(x,y,color = 'red')
        plt.ylim(0,100)
        plt.xlabel('SENTIMENTS')
        plt.ylabel('VALUES')
        plt.title('RATING')
        strFile = "C:\\Users\Shaikh\BE PROJECT\static\p3.png"
        if os.path.isfile(strFile):
           os.remove(strFile)   # Opt.: os.system("rm "+strFile)
        plt.savefig(strFile)
        plt.show()


        #Graph4

        

        x = ["NEGATIVE","NEUTRAL","POSITIVE"]
        y = [a,b,c]
        
        # plotting the points 
        plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
                        marker='o', markerfacecolor='blue', markersize=12) 

        # setting x and y axis range 
        plt.ylim(0,100) 
         

        # naming the x axis 
        plt.xlabel('SENTIMENTS') 
        # naming the y axis 
        plt.ylabel('VALUES') 

        # giving a title to my graph 
        plt.title('RATINGS') 

        # function to show the plot 
        
        strFile = "C:\\Users\Shaikh\BE PROJECT\static\p4.png"
        if os.path.isfile(strFile):
           os.remove(strFile)   # Opt.: os.system("rm "+strFile)
        plt.savefig(strFile)
        plt.show()
    
        return render_template('hi.html')







    

        



    


    









if __name__ == '__main__':
    
    app.run(debug = True, use_reloader=False)
    

