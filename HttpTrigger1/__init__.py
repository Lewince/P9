import logging
import azure.functions as func
import json

def main(req: func.HttpRequest, inputblob: str) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        userid = req_body.get('userId')
    pred_list = json.loads(inputblob)
    print(pred_list)

    if userid:
        article_ids = json.dumps(pred_list[0:5])
        return func.HttpResponse(article_ids)
    else: 
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a userId in the request body for a personalized recommendation.",
             status_code=200 
        )
 