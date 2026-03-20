# FigShare-Thingy

Exploration of ETL actions across OAI-PMH XML endpoint

Do NOT run the Python script until you edit and re-save the config.json



## STUFF 



Given endpoint: 
https://api.figshare.com/v2/oai?verb=ListRecords&metadataPrefix=oai_cerif_openaire&set=portal_1148

portal_1148 is AppState


Our Site: 

https://appstate.figshare.com/articles/thesis/_For_A_Healthy_Youth_For_A_Happy_France_Sports_Leisure_and_the_French_Popular_Front/31069819?file=61021786






FIG SHARE API endpoint: 

https://api.figshare.com/v2/oai?verb=GetRecord&identifier=oai:figshare.com:article/31069819&metadataPrefix=oai_cerif_openaire


FIG SHARE API endpoint: Dublin Core
https://api.figshare.com/v2/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:figshare.com:article/31069819


Different ID: This shows the raw-dog data. 
view-source:https://api.figshare.com/v2/oai?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:figshare.com:article/31069795


GOAL: 

Fig Share -> OCLC 
Done through MarcXML


