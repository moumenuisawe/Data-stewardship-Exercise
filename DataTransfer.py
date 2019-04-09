def cleanData(data):
    if (data.isnull().sum()):
        dataMedian = data.median()
        data.fillna(dataMedian, inplace=True)
        print("clean was done")
def calculateTheAverageOfUnEmployeeRate(pureListToCalculateTheAverage):
    averageRate = []
    year = []
    currentYear = pureListToCalculateTheAverage["DATE"][0]
    counter = 1
    sumation = 0

    for item in pureListToCalculateTheAverage["DATE"]:
        if counter % 12 == 0:
            averageRate.append(sumation / 12)
            counter += 1
            sumation = 0
            year.append(currentYear)
            currentYear +=1
        else:
            counter += 1

        if counter == len(pureListToCalculateTheAverage["DATE"]):
            break

        sumation += pureListToCalculateTheAverage["RATE"][counter]
    return  {"year":year , "rate":averageRate}


def calculateTheAverageOfMovieScoreByYear(MovieDataSet):
    scores = []

    base = MovieDataSet["year"][0]

    year =[base]
    pointer = 0
    counter = 0
    listToReturn = {}
    summation = 0
    for item in MovieDataSet["year"]:
       if item == None :
           break
       if base != MovieDataSet["year"][pointer]:
           base =  MovieDataSet["year"][pointer]
           scores.append(summation/counter)
           summation = 0
           counter = 0
           year.append(base)

       summation += MovieDataSet["score"][pointer]
       pointer +=1
       counter +=1
    scores.append(summation/counter)
    listToReturn["year"] = year
    listToReturn["score"] = scores
    return listToReturn

def getMinimumYearToBegin(firstData, secondeData):
    firstDataYearMinmimam = min(firstData["year"])
    secondeDataYearMinmimam = min(secondeData["year"])
    return max(firstDataYearMinmimam,secondeDataYearMinmimam)
def getMaxmeumYearToBegin(firstData, secondeData):
    firstDataYearMaxmum = max(firstData["year"])
    secondeDataYearMaxmum = max(secondeData["year"])
    return min(firstDataYearMaxmum,secondeDataYearMaxmum)



def cutUnwantedData(firstData,secondeData):


    minim = getMinimumYearToBegin(firstData, secondeData)
    maximum = getMaxmeumYearToBegin(firstData, secondeData)
    removeFromList(secondeData, "year", "score", maximum, minim)
    removeFromList(firstData, "year", "rate", maximum, minim)



def removeFromList(data,firstColoum,secandColoum, maxmum,minimum):

        index = 0
        while data[firstColoum][index] < minimum :
            data[firstColoum].pop(0)
            print(data[secandColoum].pop(0))




        for item in data[firstColoum]:
            if item > maxmum     :
                index = data[firstColoum].index(item)
                data[firstColoum].remove(item)
                data[secandColoum].pop(index)

            if item < minimum :
                index = data[firstColoum].index(item)
                data[firstColoum].remove(item)
                data[secandColoum].pop(index)
                print(item)
