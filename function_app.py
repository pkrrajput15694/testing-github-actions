import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
a=20
b=30
c=a+b
@app.route(route="func-testingfunc")
def func_testingfunc(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"We ahve first created Function App This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response. sum of a+b={c}",
             status_code=200
        )