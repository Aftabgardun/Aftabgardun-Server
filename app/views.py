from app import app, models, db
from flask import request, Response, render_template
import json, datetime, random


responseNotFound = '{code:1,message="Not found"}'
responseInvalidInput = '{code:1,message="Invalid input"}'

@app.route('/')
@app.route('/index')
def index():
    return "In7sN2da9E2d920"
    

@app.route('/getpersoninfo/', methods=['POST'])
def getPersonInfo():
    personid = request.form.get('personID')
    
    if (personid is not None and type(personid) == str):
        person = models.Person.objects(pk=personid).first()
        if (person is not None):
            ret = {"code":0}
            ret["name"] = person.name
            ret["papers"] = [
                            {
                             "title": i.title,
                             "paperid": str(i.id), 
                             "authors": [{"name": j.name, "personid": str(j.id)} for j in i.authors], 
                             "date": str(i.date), 
                             "keywords": ", ".join(i.keywords),
                             "publicationtype": i.publicationtype
                             }
                             for i in person.papers]
            ret["birthdate"] = person.birthdate
            ret["photo"] = person.photo
            ret["occupation"] = person.occupation
            ret["email"] = person.email
            ret["organizations"] = [{"name": i.name, "organizationid": str(i.id)} for i in person.organizations]
            ret["webpages"] = [str(i) for i in person.webpages]
            ret["keywords"] = [str(i) for i in person.keywords]
            
            return Response(json.dumps(ret))
        else:
            return Response(responseNotFound), 504
    else:
        return Response(responseInvalidInput), 504
        
@app.route('/search/', methods=['POST'])
def search():
    query = request.form.get('query')
    cat = request.form.get('cat')
    offset = request.form.get('offset', 0)
    
    if (query is not None and type(query) == str and
        cat is not None and type(cat) == str
        ):
        if (query != ""):
            if (cat == "person"):
                persons = models.Person.objects(name__icontains=query)
                l = [{"name": i.name, "personid": str(i.id), "occupation": i.occupation} for i in persons]
                ret = {"code": 0, "results": l}
                
                return Response(json.dumps(ret))
            elif (cat == "paper"):
                papers = models.Paper.objects(title__icontains=query)
                l = [{
                             "title": i.title,
                             "paperid": str(i.id), 
                             "authors": [{"name": j.name, "personid": str(j.id)} for j in i.authors], 
                             "date": str(i.date), 
                             "keywords": ", ".join(i.keywords),
                             "publicationtype": i.publicationtype
                             } for i in papers]
                ret = {"code": 0, "results": l}
                
                return Response(json.dumps(ret))
            elif (cat == "org"):
                orgs = models.Organization.objects(name__icontains=query)
                l = [{"name": i.name, "orgid": str(i.id), "description": i.description} for i in orgs]
                ret = {"code": 0, "results": l}
                
                return Response(json.dumps(ret), )
            else:
                return Response(responseInvalidInput), 504
        else:
            return Response(responseInvalidInput), 504
    else:
        return Response(responseInvalidInput), 504

@app.route('/getpaperinfo/', methods=['POST'])
def getPaperInfo():
    paperid = request.form.get('paperID')
    
    if (paperid is not None and type(paperid) == str):
        paper = models.Paper.objects(pk=paperid).first()
        if (paper is not None):
            ret = {"code":0}
            ret["title"] = paper.title
            ret["digest"] = paper.digest
            ret["date"] = paper.date
            ret["publisher"] = paper.publisher
            ret["content"] = paper.content
            ret["keywords"] = [str(i) for i in paper.keywords]
            ret["publicationtype"] = paper.publicationtype
            ret["authors"] = [{"name": i.name, "personid": str(i.id)} for i in paper.authors]
            ret["content"] = paper.content
            ret["citedby"] = len(paper.citedby)
            
            return Response(json.dumps(ret))
        else:
            return Response(responseNotFound), 504
    else:
        return Response(responseInvalidInput), 504
        
@app.route('/getorginfo/', methods=['POST'])
def getOrgInfo():
    orgid = request.form.get('orgID')
    
    if (orgid is not None and type(orgid) == str):
        org = models.Organization.objects(pk=orgid).first()
        if (org is not None):
            ret = {"code":0}
            ret["name"] = org.name
            ret["location"] = org.location
            ret["webpage"] = str(org.webpage)
            ret["photo"] = str(org.photo)
            ret["members"] = [{"name": i.name, "personid": str(i.id)} for i in org.members]
            
            return Response(json.dumps(ret))
        else:
            return Response(responseNotFound), 504
    else:
        return Response(responseInvalidInput), 504

