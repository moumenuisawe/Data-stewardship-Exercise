import  csv

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
        score = []
        counter = 0
        summetion = 0
        base = MovieDataSet["year"][0]
        print(base)
        year = [base]
        index = 0
        for item in MovieDataSet["year"]:
            print(base)

            if item == None:
                break

            if base != item:
                base = item
                print(base)
                year.append(base)
                score.append(summetion/counter)
                counter = 0
                summetion = 0
            counter +=1
            index +=1
            summetion += MovieDataSet["score"][index]
            print(score)
            return  {"year":year,"score":score}





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
                data[secandColoum].pop(0)




        for item in data[firstColoum]:
            if item > maxmum     :
                index = data[firstColoum].index(item)
                data[firstColoum].remove(item)
                data[secandColoum].pop(index)

            if item <= minimum :
                index = data[firstColoum].index(item)
                data[firstColoum].remove(item)
                data[secandColoum].pop(index)


# def createOneDictionaryfromTwo(firstDictionary,secondeDictionary):

def createFinalDictionary(firstDictionary,secDictionary):
    finalDictionary = {}
    finalDictionary["year"]  = firstDictionary["year"]
    finalDictionary["UnEmployeeRate"] = secDictionary["rate"]
    finalDictionary["movieScore"] = firstDictionary["score"]
    return  finalDictionary


def csvWriterFromDict(dictionray,filePath):
    csv_columns = ['year', 'UnEmployeeRate', 'movieScore']
    dict_data = dictionray
    csv_file = filePath
    index = 0
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            while index < len(dict_data["year"]):
                year = str(dict_data["year"][index])
                unEmployeeRate = str(dict_data["UnEmployeeRate"][index])
                movieScore = str(dict_data["movieScore"][index])

                csvfile.write(year+","+unEmployeeRate+","+movieScore+"\n")
                index +=1
    except IOError:
        print("I/O error")