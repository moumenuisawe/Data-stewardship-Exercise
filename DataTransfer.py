def cleanData(data):
    if (data.isnull().sum()):
        dataMedian = data.median()
        data.fillna(dataMedian, inplace=True)
        print("clean was done")
def calculateTheAverageOfUnEmployeeRate(pureListToCalculateTheAverage):
    listToReturn = []

    counter = 1
    sumation = 0

    for item in pureListToCalculateTheAverage["DATE"]:
        if counter % 12 == 0:
            listToReturn.append(sumation / 12)
            counter += 1
            sumation = 0
        else:
            counter += 1

        if counter == len(pureListToCalculateTheAverage["DATE"]):
            break

        sumation += pureListToCalculateTheAverage["RATE"][counter]
    return  listToReturn


def calculateTheAverageOfMovieScoreByYear(MovieDataSet):
    listToReturn = []
    sumation = 0
    base= MovieDataSet["year"][0]
    pointer = 0



