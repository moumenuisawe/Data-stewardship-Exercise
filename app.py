
import pandas as pd
import DataTransfer as df

# read files
Movies = pd.read_csv("Data/Raw/movies.csv",usecols=["year","score"])
UnEmployee = pd.read_csv("Data/Raw/unemployee.csv",usecols=["DATE","RATE"],parse_dates=True)
#  end of read files section


#  clean data to ensure that there is no null value  in it
df.cleanData(Movies["score"])
df.cleanData(Movies["year"])
df.cleanData(UnEmployee["DATE"])
df.cleanData(UnEmployee["RATE"])

#  convert date to get just year
UnEmployee["DATE"] =  pd.to_datetime(UnEmployee['DATE'], format= "%d/%m/%Y")
UnEmployee["DATE"] = UnEmployee["DATE"].dt.year
#  end of converting date section

averageUnEmployeeRate = df.calculateTheAverageOfUnEmployeeRate(UnEmployee)
averageMoviesRatePerYear = df.calculateTheAverageOfMovieScoreByYear(Movies)
df.cutUnwantedData(averageUnEmployeeRate,averageMoviesRatePerYear)
#
averageMoviesRatePerYear["year"].pop(0)
averageMoviesRatePerYear["score"].pop(0)


csvData = df.createFinalDictionary(averageMoviesRatePerYear,averageUnEmployeeRate)

df.csvWriterFromDict(csvData,"Data/processed/result.csv")


