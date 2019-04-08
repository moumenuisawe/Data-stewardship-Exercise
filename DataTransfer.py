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

def compareAndTransferData(firstData, secondeData):
    firstDataYearMinmimam = min(firstData["year"])
    firstDataYearMaxmum = max(firstData["year"])
    secondeDataYearMinmimam = min(secondeData["year"])
    secondeDataYearMaxmum = max(secondeData["year"])
    minValueToCut = max(firstDataYearMinmimam,secondeDataYearMinmimam)
    maxValueToCut = min(firstDataYearMaxmum,secondeDataYearMaxmum)
    print("min =",minValueToCut)
    print("max =",maxValueToCut)

