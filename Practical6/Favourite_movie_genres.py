#creat a dictionary to record data.
#use the for loop to print the dictionar.

#use three variables to store data 
#use the plt.pie to draw the figure

#use input() to gain the opinion of the user
#Link to the corresponding value through the dictionary

Favourite_movie_genres = {'Comedy':73, 'Action':42, 'Romance':38,
                          'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12,
                          'History':8, 'War':7}

for key in Favourite_movie_genres.keys():
    value =  Favourite_movie_genres[key]
    print("key:", key, "; value:", value)




import matplotlib.pyplot as plt         
types = 'Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War'
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=types, autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()

 #Interactive variable
a = input('please give me a type of movie: ' )         
print('the number of students who prefer', a, 'is', Favourite_movie_genres[a])





