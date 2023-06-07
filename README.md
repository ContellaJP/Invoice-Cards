The web app will return a DataFrame converted to dict that provides all the relevant rows depending on what is searched.
Search Params: invoice_type_code: 807-808 and cat_id: 1-12

Technologies:
The technologies that were used are FastAPI as the framework, and Pandas to handle the data and to allow me to simply load the csv into memory and query it from there. I understand that this is not very applicable in a large scale situation, but for this size it's perfectly fine. I used FastAPI because I heard good things about it a while ago and wanted to try it out over my usual, Flask.

Challenges:
The main thing that I ran into was the lack of time that I had to complete this, if there was more time then I would have used a database and done a frontend in React rather than just using pandas to convert the dataframe to html.

To install and run there isn't much to it:
download FastAPI, pandas, uvicorn

To run the server type:
uvicorn main:app --reload

If additional help is needed or I missed something: https://fastapi.tiangolo.com/tutorial/first-steps/

To test by categoryID: Ex. http://127.0.0.1:8000/category/?cat_id=8 <=if you'd like to search catid 8 (valid range = 1-12)
To test by invoice type code: Ex. http://127.0.0.1:8000/invoice/?invoice_type_code=808 <=if you'd like to search invoice type code 808(valid range = 807-808)


Note: I changed the excel sheet to a csv and changed the name to "GetInvoiceOptions_FC_933_6992761995 csv.csv"


The fastAPI /docs is the best way to test: http://127.0.0.1:8000/docs







