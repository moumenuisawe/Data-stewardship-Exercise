 
# Correlating Movies score and Unemployed rate

  This experiment aims to explore the connection between Movies score and Unemployed rate in the USA.


## Data Sources

* Unemployed Rate. [Data set]. https://fred.stlouisfed.org/series/LNS14000024
* Alcohol Consumption: OECD (2018), Alcohol consumption (indicator). doi: 10.1787/e6895909-en (Accessed on 22 March 2018) via https://data.oecd.org/healthrisk/alcohol-consumption.htm

The cited data sources have already been added to this repository. 



## This Project  works on this structure
![System Architecture Diagram](https://github.com/moumenuisawe/Data-stewardship-Exercise/blob/master/decumentation/architecture.png "System Architecture Diagram")





## Running the code

To run the code in this repository you will need to have access to a machine running `python` 
you should clean data before you start visualize it 
* Open Command line:   Start menu -> Run  and type cmd
* Type:   C:\python27\python.exe Exercise\app.py
* Or if your system is configured correctly, you can drag and drop your 
script from Explorer onto the Command Line window and press enter.

then you can visualize the date running Exercise/DataVisualization.py
the result will gonna be in reports file
### Docker

Run `docker build .` to create a docker image of this repository. The resulting image exposes the jupyter notebook on port `8888`.

Boot a docker container via `docker run -i -p 8888:8888 <IMAGE_ID>` to start a jupyter instance. The resulting console output will show the url you can open in your browser to take a look at the code, e.g.

```
 Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://0.0.0.0:8888/?token=<SOME_TOKEN>
```


