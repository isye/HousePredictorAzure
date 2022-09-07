git clone git@github.com:isye/HousePredictorAzure.git
cd HousePredictorAzure
make all
az webapp up --name ia-housepriceapi --resource-group iaDevops --runtime "PYTHON:3.7"
