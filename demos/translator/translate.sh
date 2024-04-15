curl -X POST "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from=ja&to=en" \
-H "Ocp-Apim-Subscription-Key: ${AI_SERVICE_KEY}" \
-H "Ocp-Apim-Subscription-Region: ${AI_SERVICE_LOCATION}" \
-H "Content-Type: application/json; charset=UTF-8" \
-d "[{ 'Text' : 'こんにちは、みんな！ お会いできてうれしいです。 あなたが住んでいる場所の天気はどうですか？' }]"
