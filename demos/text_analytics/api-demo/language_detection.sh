curl -i -X POST "${LANGUAGE_SERVICE_ENDPOINT}language/:analyze-text?api-version=2022-05-01" \
-H "Ocp-Apim-Subscription-Key: ${LANGUAGE_SERVICE_KEY}" \
-H "Content-Type: application/json" \
-d \
'
{
    "kind": "LanguageDetection",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput":{
        "documents":[
            {
                "id":"1",
                "text": "Harrys Bar and Grill in Kansas City has some of the best wings in town. However the wait times can be a bit long, which is disppointing. The decor is unique, featuring statues of mythological figures like the Greek goddess Venus. You can call Harrys Bar and Grill at 456-654-8888."
            }
        ]
    }
}
'