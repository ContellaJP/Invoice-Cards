
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory = "templates")

@app.get("/invoice/", response_class=HTMLResponse)
def get_invoices(request: Request, invoice_type_code: int):
    """
    Get invoices for a specific invoice type code and render the invoice page.

    Parameters:
    - request (Request): The HTTP request object.
    - invoice_type_code (int): The invoice type code to filter the invoices.

    Returns:
    - TemplateResponse: The rendered invoice page with the filtered invoices.
    """
    df=pd.read_csv('GetInvoiceOptions_FC_933_6992761995 csv.csv')
    queried_data = df[df['ns3:InvoiceTypeCode'] == invoice_type_code]
    selected_columns = queried_data[['ns3:InvoiceTypeCode', 'ns3:InvoiceTypeDescription', 'ns3:CategoryID', 'ns3:CategoryDescription', 'ns3:SubCategoryID', 'ns3:SubCategoryDescription']]
    result = selected_columns.to_dict(orient='records')
    
    #Handling if the user inputs something that is not present in the data provided
    if queried_data.empty:
        return "No data matching the request! Please try again with a valid invoice type code. (807-808)"
    #Rendering the template providing required data {request Type: Request, result Type: dict, invoice_type_code Type: int}
    return templates.TemplateResponse("invoiceTypeCode.html", {"request": request, "invoices": result, "invoice_type_code": invoice_type_code})



@app.get("/category/")
def get_cats(request: Request, cat_id: int):
    """
    Get invoices for a specific category ID and render the invoice page.

    Parameters:
    - request (Request): The HTTP request object.
    - cat_id (int): The category ID to filter the invoices.

    Returns:
    - TemplateResponse: The rendered invoice page with the filtered invoices.
    """
    df=pd.read_csv('GetInvoiceOptions_FC_933_6992761995 csv.csv')
    queried_data = df[df['ns3:CategoryID'] == cat_id]
    selected_columns = queried_data[['ns3:InvoiceTypeCode', 'ns3:InvoiceTypeDescription', 'ns3:CategoryID', 'ns3:CategoryDescription', 'ns3:SubCategoryID', 'ns3:SubCategoryDescription']]
    result = selected_columns.to_dict(orient='records')
    
    if queried_data.empty:
        return "No data matching the request! Please try again with a valid category ID. (1-12)"
    
    #Rendering the template providing required data {request Type: Request, result Type: dict, cat_id Type: int}
    return templates.TemplateResponse("categoryID.html", {"request": request, "invoices": result, "cat_id": cat_id})

